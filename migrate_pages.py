#!/usr/bin/env python3
# 批量改造子页: 换head(fonts+外链css), 删内联<style>块, 保持内容
import re, sys

HEAD_TMPL = '''<link rel="canonical" href="{canonical}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Crimson+Pro:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@400;700&family=Ma+Shan+Zheng&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">'''

pages = {
  'weapons/index.html': ('https://pbz-loadout.pages.dev/weapons/', 'Weapons'),
  'phantom-edges/index.html': ('https://pbz-loadout.pages.dev/phantom-edges/', 'Edges'),
  'difficulty/index.html': ('https://pbz-loadout.pages.dev/difficulty/', 'Difficulty'),
  'faq/index.html': ('https://pbz-loadout.pages.dev/faq/', 'FAQ'),
}
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/site')

for path, (canonical, _) in pages.items():
    t = open(path).read()
    # 1) 删内联style块
    t2 = re.sub(r'\n<style>[\s\S]*?</style>\n', '\n', t)
    # 2) canonical行替换为模板
    t2 = re.sub(r'<link rel="canonical" href="[^"]*">', HEAD_TMPL.format(canonical=canonical), t2)
    # 3) hero感: h1前加kicker若没有(子页已有.kicker div,跳过)
    open(path, 'w').write(t2)
    ok = 'style.css' in t2 and '<style>' not in t2
    print(path, 'OK' if ok else 'CHECK')
