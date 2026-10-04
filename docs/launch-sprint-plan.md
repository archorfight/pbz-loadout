# PBZ 发售日冲刺预案（H-72 → H+72）

基准：发售日 D=2026-10-29（PS5+Steam+Epic）。H 为相对游戏实际解锁时刻的小时偏移。
注意解锁时间因平台/区而异：PS5 一般当地 00:00；Steam 全球统一（历史上多为北京时间深夜~上午）。**H-72 内第一件事：锁定各平台确切解锁时刻**（Steam 商店页倒计时=权威），把下表锚定到真实时刻。已有 cron `pbz-launch-day`（10-29 09:00 CST）自动触发，若 Steam 解锁早于 09:00，把 cron 提前到解锁前 1h。

## 0. 数据源优先级（谁最快最准）

| 优先级 | 源 | 速度 | 准确度 | 用途 |
|---|---|---|---|---|
| P0 | 游戏本体数据挖掘（Steam 预载文件、社区解包贴 Wiki） | 解锁即出 | 最高 | 数值主源 |
| P1 | 玩家协作 Google Sheet（r/PhantomBladeZero 置顶/热帖里找） | H+2~24 | 高（多人交叉） | 武器全名单+属性 |
| P2 | wiki.gg / Fextralife wiki | H+4~48 | 中（Fextralife 常有错/占位） | 补充+交叉验证 |
| P3 | r/PhantomBladeZero 新帖 + YouTube 实测 | H+1 起 | 单点、需验证 | 机制理解（Sha-Chi 公式、升级曲线） |
| 禁用 | AI 农场站（发售前就在编数的那批） | — | 不可信 | 只用作反面参照，绝不引用 |

原则：**每个数值至少两源交叉**才标 `OFFICIAL-DATA`；单源标 `UNVERIFIED` 并注来源。徽章体系从 OFFICIAL/POST-LAUNCH 升级为 `OFFICIAL-DATA / UNVERIFIED / ESTIMATED`。

## 1. 时间表

### H-72 ~ H-24（预售冲刺）
- 锁定各平台解锁时刻，校准 cron。
- 把计算器 v1 做成**数据驱动**：武器数据抽成 `site/data/weapons.json`（字段：id/name/type/slots/stats{} /source/status），页面渲染脚本从 JSON 生成。数据结构与空表先就位，发售日只换文件。
- 写好数据采集脚本骨架：`tools/fetch_sources.py`——抓 r/PhantomBladeZero new.json、wiki.gg/Fextralife 武器页 HTML→结构化，diff 出新增武器，落地到 `site/data/`。
- 干跑一遍部署链（push→CI→pages deploy）+ `verify_live.py`。
- 预载开放后（Steam 通常 H-24 内）：确认预载可下载，社区解包一般等解锁后才能解密，别指望提前拿到数值。

### H-24 ~ H-0（就绪检查）
- 复查 GSC 收录状态（coverage 覆盖率）、sitemap 提交、首页倒计时逻辑（归零变 OUT NOW——已实现，验证一次）。
- 准备好"发售日快讯"页面草稿：`/news/` 加 launch 条目（发布时间写真实解锁时刻）。
- 人力就位：发售日凌晨~上午由主 session 值守（不是无人值守 cron 硬跑——首次数据结构未知，cron 只做"叫醒+采集"，页面更新人工/主 agent 审核后部署）。

### H-0 ~ H+6（抢首波）
- H-0：倒计时页自动切 OUT NOW；首页加"数据采集中，实时更新"横幅。
- H+0~2：刷 r/PhantomBladeZero / Steam 社区 / wiki.gg，抓任何已出武器名单；先上**名单+类型**（无需数值），把 confirmed 页升级为真名单页，每条标 `CONFIRMED IN-GAME`。
- H+2~6：首批属性数据（Sheet/wiki）出来后，weapons.json 填第一版（哪怕只有 10 把武器），上线 `/weapons/db/` 对比表 v1：属性并排+排序+筛选，不含伤害计算。

### H+6 ~ H+72（计算器转正）
- H+6~24：补齐主武器/幻刃数据；上四槽配装示意（2主+2幻刃选择器）。
- H+24~48：若 Sha-Chi/伤害公式已被社区反推出，上 damage calculator v1（公式标 `COMMUNITY-DERIVED, 待验证`）；没有公式就先做 DPS 静态对比（攻击力×攻速这类无争议计算）。
- H+48~72：sweep 一次：sitemap 重新生成（新页入图）、GSC 手动提交新 URL、内链补齐（首页→db→各武器详情页）、每页 last-updated 更新。
- 全程纪律：每次部署前跑 `verify_live.py`；数据文件 git commit message 注来源 URL。

## 2. 采集→上线工作流（谁做、怎么验证、多久）

```
采集（hermes agent 定时/手动刷源） → tools/fetch_sources.py 结构化 → site/data/*.json
  → 人工/主 agent 审核（两源交叉、徽章标注） → 渲染脚本生成页面 → push 触发 CI 部署
  → verify_live.py + curl 冒烟 → GSC 提交新 URL
```

- **谁采集**：发售窗口内主 agent session 值守 + 现有 cron `pbz-launch-day` 做启动/提醒；不新增无人值守写操作。
- **怎么验证**：数值两源交叉；单源数据页脚列 source URL；`verify_live.py` 扩展断言（每个武器条目必有 status 徽章、必非空 stats）。
- **多久上线**：名单类 H+2~6；属性表 H+6 内第一版；计算器 H+24~48。单次"采集→部署"循环目标 ≤1h（数据文件化后就是改 JSON+push）。

## 3. 发售前 25 天（10-04 ~ 10-28）还能做什么

按周排：
- **W1（10-04~10-10）**：
  - 数据层重构：weapons.json schema 定稿 + 页面改数据驱动（上面 P0 项）。
  - GSC 收尾（skill 待办3）：确认 sitemap 已提交、抽查收录；零收录则查技术面。
  - pages.dev→apex 301 复核（待办4）。
- **W2（10-11~10-18）**：
  - 关键词布局落地：`best weapons`/`weapon tier list`/`builds`/` phantom edges list` 等 landing 骨架页（内容=系统讲解+倒计时+「发售后填实测」，noindex 或薄页暂不进 sitemap，发售日填真数据再放开）。
  - schema：现有 VideoGame/FAQPage/Breadcrumb 之外，给 confirmed 名单页加 ItemList；预留每武器详情页的 Article/VideoGame 项模板。
  - AdSense 申（待办5，赶流量季）。
- **W3（10-19~10-25）**：
  - 对标 maxroll/game8 赢家标配复查（事实表/FAQ/内链网），补缺口页。
  - 采集脚本 dry-run（拿别的游戏 sub/wiki 练手验证解析器）。
  - 计算 CSS/交互的对比表+筛选 UI 先做好，空数据状态下不破版。
- **W4（10-26~10-28）**：只做就绪检查，不动结构（冻结期）。全链路演练一次假数据部署+回滚。

## 4. 风险预案

**数据比预期复杂**（武器带形态/升级分支/词条随机）：
- 不等全量：先上「基础属性对比表」，复杂维度（形态/词条）标 `POST-LAUNCH PHASE 2`，分批上。
- 计算器降级为「静态对比+排序筛选」，伤害公式后补。

**数据比预期简单**（属性维度少）：
- 竞品会更快做出表格 → 差异化转向：四槽配装保存/分享（URL 编码 loadout）、配装推荐内容、更新频率（数据打时间戳，抢"最新版本"信任）。

**数据出得慢（H+72 仍无结构化数据）**：
- 用 YouTube 实测逐条录入（哪怕 10 把武器 8 个属性），每条标来源视频；同时首页横幅改「数据持续录入中」维持诚实牌。
- 绝不为了抢速度编数或引用农场站——诚实牌是唯一差异化。

**解包数据与游戏内显示不一致 / 首日补丁改数值**：
- 数据文件带 `patch_version` 字段；发现 patch 重刷；页面显示「数据版本：首日补丁后」。

**服务器/部署事故**：CF Pages 回滚到上一 commit；pages.dev 与 apex 双域名都可访问兜底。
