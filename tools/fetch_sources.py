#!/usr/bin/env python3
"""PBZ launch-day source fetcher — collects weapon data leads, never publishes.

Workflow (see docs/launch-sprint-plan.md):
  python3 tools/fetch_sources.py            # fetch all sources → reports/
  python3 tools/fetch_sources.py --diff     # compare vs last run, print new weapon names

Sources: r/PhantomBladeZero new.json (P0 community), wiki.gg / Fextralife (P2 cross-check).
AI-farm sites are NEVER fetched (blacklist below). Every candidate gets a source URL;
publishing still requires two-source cross-check by the human/main-agent reviewer.

Network note: this machine reaches reddit/wikis via the shared Chrome (browser-serial)
when plain curl is blocked — fetch_sources falls back to old.reddit .json over HTTPS
first, and reports clearly which source failed so the operator can drive the browser.
"""
import json
import os
import re
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_DIR = os.path.join(ROOT, "reports")
STATE_FILE = os.path.join(REPORT_DIR, "seen_names.json")

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) pbz-loadout-fetcher/1.0"}
BLACKLIST = ("fandom-china", "ai-farm")  # never fetch; extend on sight

SOURCES = [
    {
        "id": "reddit-phantombladezero",
        "kind": "reddit-new",
        "url": "https://old.reddit.com/r/PhantomBladeZero/new.json?limit=50",
        "priority": "P0",
    },
    # wiki.gg / fextralife weapon pages: add exact URLs once the game's wiki
    # namespace is known at launch (they do not exist pre-launch). Placeholder
    # entries keep the pipeline shape ready — fill "url" on launch day.
    # {"id": "wikigg-weapons", "kind": "html-table", "url": "", "priority": "P2"},
    # {"id": "fextralife-weapons", "kind": "html-table", "url": "", "priority": "P2"},
]

# Weapon-name heuristics: known canon words from trailers + generic weapon nouns.
WEAPON_WORDS = re.compile(
    r"\b(sword|blade|saber|katana|dao|spear|lance|staff|rod|axe|hammer|mace|dagger|"
    r"scythe|whip|bow|crossbow|gun|cannon|fist|claw|halberd|glaive|rapier|edge)\b",
    re.IGNORECASE,
)


def get(url: str, timeout: int = 15):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def fetch_reddit(src):
    """Return list of {title, url, score, created} candidate posts."""
    try:
        data = json.loads(get(src["url"]))
    except Exception as e:  # noqa: BLE001
        return {"error": "%s: %s" % (src["id"], e), "items": []}
    items = []
    for c in data.get("data", {}).get("children", []):
        d = c.get("data", {})
        items.append(
            {
                "title": d.get("title", ""),
                "url": "https://old.reddit.com" + d.get("permalink", ""),
                "score": d.get("score", 0),
                "comments": d.get("num_comments", 0),
                "created": d.get("created_utc", 0),
            }
        )
    return {"error": None, "items": items}


def weaponish(title: str) -> bool:
    return bool(WEAPON_WORDS.search(title or ""))


def main():
    only_diff = "--diff" in sys.argv
    os.makedirs(REPORT_DIR, exist_ok=True)
    run_id = time.strftime("%Y%m%d-%H%M%S")

    all_items, errors = [], []
    for src in SOURCES:
        if not src.get("url"):
            continue
        if src["kind"] == "reddit-new":
            res = fetch_reddit(src)
        else:
            res = {"error": "%s: kind %s not implemented yet" % (src["id"], src["kind"]), "items": []}
        if res["error"]:
            errors.append(res["error"])
        for it in res["items"]:
            it["_src"] = src["id"]
            it["_prio"] = src["priority"]
        all_items.extend(res["items"])

    candidates = [i for i in all_items if weaponish(i.get("title", ""))]

    seen = {}
    if os.path.exists(STATE_FILE):
        seen = json.load(open(STATE_FILE))
    new = [i for i in candidates if i["title"] not in seen]

    if not only_diff:
        report = {
            "run": run_id,
            "fetched": len(all_items),
            "weapon_candidates": len(candidates),
            "new_candidates": len(new),
            "errors": errors,
            "candidates": sorted(candidates, key=lambda x: -(x.get("score") or 0))[:40],
        }
        path = os.path.join(REPORT_DIR, "fetch-%s.json" % run_id)
        json.dump(report, open(path, "w"), indent=2, ensure_ascii=False)
        print("report: %s (%d candidates, %d new, %d errors)" % (path, len(candidates), len(new), len(errors)))

    print("\n== NEW weapon-name leads (%d) ==" % len(new))
    for i in sorted(new, key=lambda x: -(x.get("score") or 0))[:20]:
        print("[%s|%s] %s\n  %s" % (i["_prio"], i["_src"], i["title"], i["url"]))

    for i in candidates:
        seen[i["title"]] = run_id
    json.dump(seen, open(STATE_FILE, "w"), ensure_ascii=False)
    if errors:
        print("\nWARN failed sources:", *errors, sep="\n  ")
        print("(If reddit curl is network-blocked, drive the shared Chrome via "
              "browser-serial and save the .json into reports/ manually.)")


if __name__ == "__main__":
    main()
