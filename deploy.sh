#!/bin/bash
# pbz-loadout 部署脚本 — CF Pages 直传项目无 Git 集成(硬规则), push 不触发部署
# 用法: 改完 site/ 下文件 -> ./deploy.sh  (自动 commit+push+wrangler 部署)
set -e
cd "$(dirname "$0")"
if ! git diff --quiet --cached && ! git diff --quiet; then
  git add -A
  git commit -m "deploy: $(date +%m%d-%H%M)" || true
fi
git push origin main || echo "push失败(继续部署)"
npx wrangler pages deploy site --project-name pbz-loadout --branch main
echo "--- 验证:"
sleep 20
curl -s -m 15 https://www.pbzloadout.xyz/ -o /dev/null -w "线上: %{http_code}\n"
