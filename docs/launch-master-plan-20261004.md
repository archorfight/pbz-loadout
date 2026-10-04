# PBZ 发售冲刺总方案（2026-10-04 三方合并终版）

输入：Hermes 一手调研 + 预案 agent（数据源/工作流）+ 评估 agent（关键词/页面矩阵，其 Autocomplete 结论已独立复核 ✅）

## 核心战略修正（评估 agent 提出并验证，采纳）

**主攻词改为 weapons list + bosses，calculator 降级为辅助**：
- bosses 10 个 autocomplete 变体（全站最热）、weapons 5 变体——真实需求
- damage calculator / best weapon 零变体=Google 层面无搜索行为沉淀
- "搜索位真空≠需求真空"——之前把 calculator 当核心是最大判断风险
- 农场站占着 best weapon/tier list 但数据是编的 → 发售日=他们的死期=我们的入场券

## 发售前 25 天（10-04 → 10-28）任务清单

### P0 工程（10-10 前完成）
1. **weapons.json 数据驱动改造**：武器数据抽离成 JSON，页面数据驱动渲染——发售日只换 JSON+push，单循环 ≤1h 上线（这是发售日速度的生命线）
2. **新增 /bosses/ 页**：已公开 boss 名单（宣传片/demo 逐个列，SHOWN 徽章，只用官方确证素材）
3. **新增 /guides/trophy-guide/ 页**：官方已公布成就列表
4. **首页/nav C 位调整**：calculator → weapons + bosses
5. **修 apex 根域 000**：用户 CF dashboard 建 zone（API 无权限，需用户点）或维持 www-only（canonical 已指 www，不阻塞）

### P1 内容（10-10 → 10-20）
6. /weapons/confirmed/ 名单页完善（SHOWN 徽章体系）
7. /guides/walkthrough/ 壳页（章节目录结构，内容 POST-LAUNCH）
8. /calculator/ 壳页挂 POST-LAUNCH 徽章，保留但不投首页权重

### P2 收尾（10-20 → 10-28）
9. H-72 内：锁 Steam 真实解锁时刻，校准 launch cron（现在锚 09:00 CST 可能偏晚）
10. GSC 索引复查（10-10 数据出来后：无收录页逐个"请求编入索引"，配额 10-12/天分两轮）
11. schema.org VideoGame + FAQ 结构化数据补全

## 发售日时间表（H=解锁时刻）

| 时点 | 动作 |
|---|---|
| H-72 | 校准 cron 时刻；weapons.json 占位结构就绪 |
| H+0~2 | 开游戏，抓武器/boss 初见名单 |
| H+2~6 | 真名单页上线（All Weapons Complete List + All Bosses in Order） |
| H+6~12 | 属性对比表 v1（基础攻击/防御/特效词条，两源交叉） |
| H+24~48 | 计算器/对比器（视数据深度：数值深→伤害计算，浅→A vs B 对比表+滤镜） |
| H+48~72 | 社区反馈修正轮 |

**数据源优先级**：P0 游戏本体 → P1 r/PhantomBladeZero 社区 Sheet → P2 wiki.gg/Fextralife → P3 YouTube 实测。每数值两源交叉。AI 农场站（已列名单）一律禁用为源。徽章体系：OFFICIAL-DATA / COMMUNITY-VERIFIED / UNVERIFIED。

## 首周（10-29 → 11-04，生死周）
- 每把武器一页、每个 boss 一页（招式表+应对+掉落）持续填充
- 发售日当天两篇主打文：All X Weapons / All Bosses in Order
- tier list 等真数据 ≥10 把后再上（这时才有资格打农场站）

## 退路（数值系统简单时，按优先级）
1. boss wiki 主转型（需求最大，不依赖数值深度）
2. build/loadout tier list（配装组合推荐，匹配域名本意）
3. calculator 降为属性对比辅助工具

## 复核点
- 10-10：GSC 索引数据 + apex 修复
- 10-26：发售前全站演练（换一份假 weapons.json 走全流程计时）
