#!/usr/bin/env python3
# pbz-loadout 线上断言: canonical/OFFICIAL徽章/FAQPage schema (skill#23 纪律)
import urllib.request, ssl, sys
ctx = ssl.create_default_context()
def get(u):
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (pbz-verify)"})
    with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
        return r.read().decode("utf-8", "ignore")

checks = []
home = get("https://pbz-loadout.pages.dev/")
checks.append(("canonical→pages.dev", 'href="https://pbz-loadout.pages.dev/"' in home))
weapons = get("https://pbz-loadout.pages.dev/weapons/")
checks.append(("weapons OFFICIAL badges", weapons.count("OFFICIAL") >= 4))
faq = get("https://pbz-loadout.pages.dev/faq/")
checks.append(("FAQPage JSON-LD", "FAQPage" in faq))
checks.append(("data policy notice", "We will not invent stats" in home))

fails = [n for n, ok in checks if not ok]
for n, ok in checks:
    print(("PASS " if ok else "FAIL ") + n)
sys.exit(1 if fails else 0)
