# PBZ Loadout — v3 之后改进清单（improvements-v4）

日期：2026-10-02 ｜ 发售日：2026-10-29（距今 27 天）
现状：v3 改版已完成（满版 key art hero / 毛玻璃卡片 / 渐变红 CTA / Space Grotesk），视觉复查 8.5/10。
已知扣分点：区块间留白偏大、卡片缺微交互、页脚简陋、下半页视觉密度不足。

---

## 0. 竞品调研摘要（信息源）

调研对象与 takeaway：

| 站点 | 设计/结构亮点 | 预热期策略 | 对我们的启示 |
|---|---|---|---|
| **maxroll.gg** | 极简干净 + 全站强搜索（自定义索引器）、每游戏子站、dark 主题统一、卡片信息密度高、内部互链成网 | 发售前密集发"系统指南/职业预览"，每篇都是可长期吃 SEO 的常青页 | 搜索是回头用户第一入口；预热期就把"系统解释页"铺满 |
| **game8.co** | 每页顶部"Product Information"事实表（发售日/平台/容量/开发商）、Latest News 区块、FAQ 常驻、目录式导航 | 发售前以官方情报整理 + 新闻时间线为主，事实表吃精选摘要 | 事实表极易拿 Google rich result；新闻时间线页是预售期合规内容主力 |
| **poe2db.tw** | 纯数据站，首页就是倒计时（league start/end）、表格式高密度、更新极快 | 补丁一出当天更新数据 | 首页倒计时是数据站标配钩子；发售日"数据当天上线"就是护城河 |
| **PBZ 同赛道竞品**（phantombladezero.world / phantombladezerowiki.org 等） | 部分已列出 14 把已确认武器名（Sanguine、Juggernaut、Seamless Death 等）并标注来源 | 抢"confirmed weapons"关键词 | 我们 /weapons/ 目前只有系统说明、没有武器名单——这是最明显的内容缺口 |

共同点：赢家都是"事实表 + FAQ + 强内链 + 倒计时"四件套，而不是华丽动效。

---

## 1. 视觉 / UX 微改进（尊重现有黑 + 朱砂 + Cinzel/Space Grotesk 设计系统）

| # | 项目 | 说明 | 工作量 | 优先级 |
|---|---|---|---|---|
| V1 | 区块留白节奏收紧 | section 间距从统一大留白改为节奏化（hero→首区块紧、之后渐宽），或给下半区块加 `scroll-margin` 视觉锚；不改设计系统只调 spacing 变量 | 30min | P0 |
| V2 | 卡片微交互 | 卡片 hover：边框朱砂渐隐 + 轻微 translateY(-3px) + 内部 num 数字变色；纯 CSS，20 行内 | 20min | P0 |
| V3 | loadout-diagram 交互 | 四槽位图 hover/点击高亮对应说明（slot 联动），触屏用 tap；原生 JS ~30 行 | 40min | P1 |
| V4 | 页脚重做 | 现页脚仅两行文字。改成三列：站点导航 / 数据政策（OFFICIAL vs POST-LAUNCH 图例）/ 免责 + last-updated 日期 + 社交链接位；与 hero 同款毛玻璃卡 | 45min | P0 |
| V5 | 下半页视觉密度 | "At launch" 区块加一个 launch-day roadmap 时间轴（Oct 29 → 数据库上线 → 计算器上线），填补下半页空；复用现有 sec-tag 样式 | 60min | P1 |
| V6 | 倒计时做成活的 | hero 里 "29.10.2026" 静态文本改为真倒计时（D:H:M:S，JetBrains Mono 数字），归零时切换文案为 "OUT NOW" | 30min | P0 |
| V7 | 移动端复查 | 检查 hero-meta 在 375px 是否换行拥挤、表格横滚、nav 折叠成汉堡；纯 CSS 修正 | 40min | P1 |
| V8 | 滚动 reveal 参数微调 | threshold .08 偏灵敏，改 .15 + 少量 `transition-delay` 阶梯，避免一屏全闪现 | 10min | P2 |
| V9 | 暗链/焦点态 | 卡片内 a 现在用 inline style 去下划线——改为统一 `.card a` 类，补 `:focus-visible` 朱砂 outline（可访问性） | 20min | P2 |

## 2. 内容 / SEO 增强（预售期只写官方确认事实，不编数据）

| # | 项目 | 说明 | 工作量 | 优先级 |
|---|---|---|---|---|
| C1 | **已确认武器名单页** | 竞品已列 14 把官方露面武器（Sanguine / Sanguine Twin / Sanguine Reach / Jagged Steel / Juggernaut / Seamless Death / White Serpent & Crimson Viper / Soft Snake Sword / Venomous Softblade 等）。逐把核对官方 State of Play /预告片后列名单，每把标"首露出处+日期"，无数据字段就只写身份描述——这完全合规且是当前最大关键词缺口（"phantom blade zero weapons list"） | 120min | **P0** |
| C2 | FAQPage 结构化数据 | /faq/ 已有内容，补 JSON-LD `FAQPage` schema，争取 SERP 富摘要。其他页补 `BreadcrumbList` + `VideoGame`（发售日/平台/开发商） | 45min | P0 |
| C3 | game8 式事实表 | 首页或 /about/ 加 "Product Information" 表：发售日 2026-10-29、平台 PS5/PC(Steam/Epic)、开发商 S-GAME、类型、愿望单数——全是官方公开事实，极易被摘录 | 30min | P1 |
| C4 | 新闻/情报时间线页 | `/news/`：按时间列官方确认节点（State of Play Aug 17、发售日公布、愿望单里程碑…），每条带来源链接。预售期可持续更新，吃新鲜度信号 | 90min | P1 |
| C5 | /weapons/ 补齐已确认武器锚点 | 现在 /weapons/ 只有系统说明无名单，与 C1 互链：系统页→名单页→各武器 mini 段落 | 含在 C1 | P1 |
| C6 | sitemap + 内链网 | 确认 sitemap.xml 覆盖全部页；每页底部加 "相关指南" 交叉链接（maxroll 式内链网） | 30min | P1 |
| C7 | og/twitter 卡 | 检查各页 og:image（用 key art 裁图）、og:title 差异化——分享到 Discord/Reddit 的第一印象 | 25min | P1 |
| C8 | hreflang/语言 | 竞品多有 /en/ 前缀抢多语言；先不做多语言，但在 about 里声明英文唯一，避免重复内容 | 10min | P2 |

## 3. 转化与留存（发售日钩子）

| # | 项目 | 说明 | 工作量 | 优先级 |
|---|---|---|---|---|
| T1 | **发售日邮件/提醒订阅** | 倒计时旁加 "Get notified when the database goes live" 邮件框（用 Formspree/CF Worker + KV 存邮箱，零后端框架）。这是发售日流量变现的核心资产 | 90min | **P0** |
| T2 | 倒计时 + 解锁倒计时 | hero 双倒计时：发售倒计时 + "database goes live T-0" 文案，强化"发售日回来看数据"的心智 | 含 V6 | P0 |
| T3 | 社区引导 | 页脚/文章尾加 Discord（自建或官方服）+ Reddit r/PhantomBladeZero 引导；预售期社区内容=免费外链与回访 | 20min | P1 |
| T4 | "Launch-day checklist" 内容钩子 | 一篇预售期合规文："发售日第一天该验证什么"（武器名核对、材料返还验证…）——预告数据库能力且天然引导订阅 | 45min | P1 |
| T5 | 浏览器提醒（可选） | Notification API "发售日提醒我" 按钮，比邮件更轻；需用户手势授权，纯原生 JS | 40min | P2 |
| T6 | 预热页占位（launch 模式开关） | 提前做好 launch-day 首页变体（数据模式），发售后一键切换——避免当天手忙脚乱 | 90min | P2 |

---

## 建议执行顺序（总 ~11.5h）

1. **本周（距发售 27 天）**：V6+V1+V2+V4（视觉止血）→ C1+C2（最大内容缺口+富摘要）→ T1（邮件订阅，越早攒列表越好）
2. **下周**：C3/C4/C6/C7 + T2/T3
3. **发售前一周**：T4 + T6（launch 变体演练）+ V7 移动端终检

## 硬规则遵守确认
- 所有内容项均基于官方确认事实（State of Play、Steam 页、官方预告），未列任何未公开数值；
- 全部为纯静态 HTML/CSS/原生 JS 改动，不引入框架；
- 全部沿用现有黑+朱砂+Cinzel/Space Grotesk 设计系统与 OFFICIAL/POST-LAUNCH 徽章体系。
