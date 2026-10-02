# PBZ Loadout — 项目状态

## 站点
- 线上: https://pbz-loadout.pages.dev （CF Pages，GitHub push 自动部署）
- Repo: github.com/archorfight/pbz-loadout（secrets 已配，CI=deploy.yml）
- 2026-10-02 上线：6页壳（首页/weapons/phantom-edges/difficulty/faq/about）+ sitemap + robots
- 线上断言脚本 verify_live.py 全 PASS（canonical/徽章/FAQPage/数据政策）

## 差异化定位
- 数据诚实：OFFICIAL/POST-LAUNCH 双徽章，红字声明不编数（打AI农场竞品）
- 发售日（10-29 09:00 cron 自动触发）抓真数据 → 武器数据库+对比表 → 计算器v1

## 验证线（纪律）
- 10-29 发售日：cron 自动执行数据升级；数据源不可用时人工兜底
- 发售+2周（11-12 附近）：GSC 收录/曝光检查 → 有曝光=继续加内容；零收录=查技术面
- 圣诞季前决策点：若 PBZ 站起量，考虑买品牌域名（EMD 已全被抢注）

## 已纳入
- site-monitor 每日探活（第11个站）
- 发售日行动 cron：pbz-launch-day（2026-10-29 09:00，跑完自删）
