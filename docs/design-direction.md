# PBZ Loadout 站点氛围感改造方案 — Kung-Fu Punk 设计方向

> 目标:让 pbz-loadout.pages.dev 从"通用棕黑文档站"变成一眼可辨的 Kung-Fu Punk 武器库。
> 约束:纯 CSS 为主、字体全部免费可自托管(Google Fonts)、不使用需授权素材、不引入 JS 重框架。
> 受众:欧美主机/PC玩家(英文内容)。

---

## 1. 调研结论

### 1.1 官方视觉语言(实测 pbz.s-game.com 的 HTML/CSS 抓取)

- **底色近纯黑** `#07090a`,官方 styles.css 中几乎无浅色;层次靠黑上加黑(`#1a1a1a` 面)+ 白字 `#fff`,而非棕色系。
- **唯一的强调红** `#c23a3a`(接近朱砂/血锈红,饱和度中低,不是亮红)。官方全站仅这一个品牌色。
- **排版策略**:英文标题用衬线 Alverata(巴洛克感衬线,非 Georgia);中文/装饰用楷体(FZKaiTi 系,书法气质)。正文极简、大量留白,装饰全部交给满版 key art 影像 + 视频 poster(hero 用 `/assets/videos/home/poster/*.webp` 满铺)。
- **构图**:竖排/大字号标题、影像与渐变遮罩(`rgba(0,0,0,.8)` 底部压深)叠合,信息浮在"画面"上,而不是"文档+边框"。
- **氛围来源是影像+留白+书法字**,不是边框、圆角卡片和米金色装饰。

**结论:现站的问题** —— 棕色系(`#14100d`/`#3a2f24`/`#d4a24e` 金)是"复古皮革游戏站"套路,与 PBZ 官方的"黑+朱红+水墨"错位;Georgia 正文衬线正是历史纠偏中点名的"90年代默认感";卡片+圆角+虚线框是文档感来源。

### 1.2 游戏工具站标杆(氛围不是"贴纸",是系统)

- **Fextralife / PoEDB(工具站主流)**:共同点是"主题皮肤数据站"——统一的深底、专属于该游戏的强调色(魂系的金棕、PoE 的暗金),所有表卡同一质感,让数据页也有游戏感。反例教训:它们氛围来自"一致",不来自花哨。
- **bld.gg / maxroll 一系**:暗底 + 高对比强调色 + 大写字母间距 kicker + 等宽数字,信息密度高但气质统一,是工具站"有氛围不显老"的可行路径。
- 可借鉴核心:**一套 2-3 色的严格配色纪律 + 全站同一种卡片语言 + 一个强识别的装饰母题(这里是水墨/笔触)**。

---

## 2. 设计方向总纲

**一句话:墨黑为底、朱砂一点、宣纸残白、笔触做骨。**

三母题(贯穿全站,不做贴纸堆砌):
1. **墨(ink)**:近纯黑底 + 大颗粒噪点纸纹 + 径向墨晕,层次用"墨的深浅"而非棕色边框。
2. **朱(cinnabar)**:`#c23a3a` 一族作为全站唯一强调色,用于 kicker、数据数字、悬停、封印/印章元素。
3. **笔(brush)**:标题旁一笔笔触、卡片用笔刷撕裂边(clip-path/mask)、分隔线是不规则笔道,替代直角边框。

---

## 3. 具体规格

### 3.1 配色 token(替换现 `:root`)

```css
:root{
  /* 墨底 */
  --bg:#0b0c0e;          /* 近纯黑微冷,替代 #14100d */
  --surface:#15171a;     /* 卡面,黑上加黑 */
  --surface-2:#1c1e22;
  --border:#2a2d33;      /* 冷灰边框,替代棕色 #3a2f24 */
  /* 文字 */
  --text:#e9e6df;        /* 宣纸白 */
  --muted:#9a958a;       /* 灰褐,替代偏棕 #a89880 */
  --faint:#6b675f;
  /* 朱砂强调(全站唯一品牌色) */
  --accent:#c23a3a;      /* 官方红 */
  --accent-bright:#e0514a; /* hover/焦点 */
  --accent-dim:#7a2a2a;  /* 背景 wash */
  /* 辅助(少用) */
  --bone:#d9d2c5;        /* 数字/高亮替代金色 */
  --seal:#8f2f2f;        /* 印章暗红 */
  /* 质感 */
  --ink-shadow:0 20px 60px rgba(0,0,0,.55);
}
```

- **删除** `--gold:#e8c887` 金色系(现站 h2/链接全金,是"皮革站"感主因),标题改宣纸白+朱砂点缀。
- 对比度:bone on bg ≈ 9.5:1,accent on bg ≈ 5:1,均可读。

### 3.2 字体(Google Fonts,全部 OFL 可自托管)

| 用途 | 字体 | 说明 |
|---|---|---|
| 英文标题 | **Cinzel**(600/700) | 碑刻衬线,冷峻,贴合 killer/blade 气质,替代 Georgia 标题 |
| 英文正文 | **Crimson Pro**(400/600) | 低对比老式衬线,可读性好,替换 Georgia 正文 |
| 数据/数字/标签 | **JetBrains Mono**(400/700) | 武器数、槽位、OFFICIAL 徽章、倒计时,等宽带来的"档案感" |
| 中文点缀(可选) | **Noto Serif SC**(900) 或 **Ma Shan Zheng**(书法) | 站内少量汉字水印如「刃」「影」,Ma Shan Zheng 是毛笔楷书,更水墨 |

```html
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Crimson+Pro:wght@400;600&family=JetBrains+Mono:wght@400;700&family=Ma+Shan+Zheng&display=swap" rel="stylesheet">
```

排印细节:
- kicker 用 JetBrains Mono,`letter-spacing:.35em; text-transform:uppercase; font-size:.72rem; color:var(--accent)`。
- h1 用 Cinzel 700,`clamp(2.2rem,5vw,3.4rem)`,可对 "Zero" 一词用朱砂色。
- 大数字(30+/25/2+2)用 Cinzel 700 + `--bone`,下标签 JetBrains Mono 大写。

### 3.3 装饰元素(纯 CSS/SVG,零授权问题)

**a. 纸墨噪点纹理**(body 背景,一行 SVG feTurbulence,自托管 data URI):
```css
body{
  background:
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3CfeColorMatrix values='0 0 0 0 0.8 0 0 0 0 0.78 0 0 0 0 0.72 0 0 0 0.04 0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E"),
    radial-gradient(1200px 800px at 70% -10%, #16181c 0%, transparent 60%),
    var(--bg);
}
```

**b. 笔刷边卡片**(核心母题,用 CSS mask 模拟撕裂毛边):
```css
.card{
  background:linear-gradient(180deg,var(--surface-2),var(--surface));
  border:none;
  border-left:3px solid var(--accent-dim); /* 一抹朱,像刀口 */
  -webkit-mask-image:url("brush-edge.svg"); /* 32×32 手绘毛边 mask,可自制或用 turbulence 生成 */
  padding:26px 24px;
}
.card:hover{ border-left-color:var(--accent); transform:translateY(-2px); }
```
毛边 mask 可用 SVG feTurbulence+displacement 自制一次,全站复用,不依赖外部素材。

**c. 水墨晕 wash**:hero 与 section 背景叠加 `radial-gradient(closest-side, rgba(194,58,58,.08), transparent)` 的大块暗红墨晕,以及 `filter: blur(80px)` 的墨团伪元素。

**d. 分隔笔道**:section 之间用不规则笔触:
```css
section{border-top:none;position:relative}
section::before{content:"";position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent,var(--faint) 15%,var(--accent) 50%,var(--faint) 85%,transparent);
  mask-image:url("rough-line.svg");opacity:.5}
```

**e. 印章徽章**:OFFICIAL / POST-LAUNCH 标志改成方形印章风:
```css
.status-flag{font-family:'JetBrains Mono';border:1px solid currentColor;border-radius:2px;
  padding:2px 8px;background:transparent}
.confirmed{color:#c96f5f;border-color:#8f4a3f}   /* 朱印 */
.pending{color:var(--muted);border-style:dashed}  /* 未落款 */
```

**f. 汉字水印**:h1/h2 侧放一个 8rem 的「刃」或「影」(Ma Shan Zheng,`opacity:.06; writing-mode:vertical-rl`),英文站里一个汉字即身份标识,不喧宾夺主。

### 3.4 Hero 构图(概念型开场:画面自己证明)

放弃"居中标题+副文+按钮"的文档式 hero,改为:

```
[全屏 100svh,背景 = 官方 key art 截图或纯 CSS 墨晕 + 剪影]
 左下角:巨型 Cinzel 标题,压在暗部
   kicker: PHANTOM BLADE ZERO — KUNG-FU PUNK (mono, 朱砂, 字距拉开)
   H1: EVERY WEAPON. EVERY LOADOUT.
   一行 Crimson Pro 副文 + JetBrains Mono 倒计时(数字大写间隔)
 右侧:竖排「刃」水印淡淡压住
 底部:一道朱砂笔道横贯,与下方内容分界
```

- 背景首选官方已公开的 trailer 截图(新闻稿/key art 属常规引用,加 © S-GAME 标注);完全零素材方案 = 多层 radial-gradient 墨晕 + 噪点 + 一个 CSS 剪影(SVG path 白发杀手背影,自绘,opacity .15)。
- 首屏只讲一件事:**"55 weapons. One killer."** —— 数字用 Cinzel 大字,画面自证氛围。

### 3.5 交互动效(纯 CSS,克制)

1. **刀光下划线**:导航/链接 hover 用 `background-size` 过渡的朱砂斜切线,`transition:.25s`。
2. **卡片入鞘**:卡片 hover 微抬 2px + 左侧刀口变亮,不缩放不发光。
3. **滚动浮现**:内容块 `@media (prefers-reduced-motion:no-preference)` 下 `animation: fade-up .6s both`(IntersectionObserver 也可用 20 行原生 JS,非框架)。
4. **数字起势**:统计数字用 CSS `@property --n` 计数动画(纯 CSS,支持面够)。
5. **倒计时呼吸**:朱砂倒计时数字 `opacity .85↔1` 缓慢呼吸,4s 周期。
- 禁用:代码雨、glitch、扫描线(历史纠偏点名),全站动效不超过上述 5 项。

---

## 4. 分层落地

### P0 — 氛围最小改动集(半天内,只动 CSS + 字体 + hero)

1. 换配色 token(§3.1):棕→黑冷灰,金→朱砂,一次性删掉 Georgia。
2. 引入 4 个 Google Fonts(Cinzel/Crimson Pro/JetBrains Mono/Ma Shan Zheng)并设字体栈。
3. body 加噪点纹理 + 墨晕背景(§3.3a)。
4. kicker/数字/徽章改 JetBrains Mono + 朱砂;h2 从金色改宣纸白。
5. 卡片:去圆角去均匀边框 → 黑面 + 左侧 3px 朱线 + hover 抬升;OFFICIAL 徽章改印章风(§3.3e)。
6. section 分隔线改渐隐笔道(§3.3d)。
7. hero 文案压到极简("55 weapons. One killer."),标题左对齐下沉,加大留白。
- 效果:70% 的氛围来自底色+字体+强调色纪律,这 7 项即完成主体。

### P1 — 完整 Kung-Fu Punk 气质(1-2 天)

1. hero 满版重构(§3.4):官方 key art/截图 + 渐变压暗 + 竖排汉字水印 + 底部朱砂笔道。
2. 笔刷毛边 mask 自制并应用到卡片/图片(§3.3b)。
3. 武器 4 槽 loadout 图改成"刀架/卷轴"隐喻:槽位用笔道分隔、配 mono 编号,中心留一个 slot 预告位。
4. 全站 5 项动效(§3.5)。
5. 页面级母题复用:每页 h2 前加统一「朱砂短线 + mono 编号」的 section 标记,建立节奏。
6. 深色 schema 微调数据表(weapons 页):表头 mono 大写、行 hover 朱砂 8% wash。

### 验收标准(对照历史纠偏)

- ✅ 无 90 年代默认样式:Georgia、米黄/棕金全部移除。
- ✅ 无 glassmorphism、无代码雨/glitch 堆砌。
- ✅ 主题气质靠字体(Cinzel/楷书)、配色(黑/朱/宣白)、真实纹理(噪点/笔触)传达,不靠贴纸。
- ✅ 视觉即主题:墨、朱、笔三母题直接对应 Kung-Fu Punk(水墨暗黑 + 朱砂武侠 + 手作质感)。
- ✅ 全部免费可自托管素材,纯 CSS 实现,无新 JS 依赖。
