#!/bin/bash
# 快速部署脚本

echo "🚀 准备部署到GitHub..."
echo ""

# 检查是否在正确的目录
if [ ! -f "README.md" ]; then
    echo "❌ 错误：请在项目根目录运行此脚本"
    exit 1
fi

echo "📋 检查必要文件..."
files_ok=true

if [ ! -f ".github/workflows/notification.yml" ]; then
    echo "❌ 缺少: .github/workflows/notification.yml"
    files_ok=false
fi

if [ ! -f "scripts/notification.py" ]; then
    echo "❌ 缺少: scripts/notification.py"
    files_ok=false
fi

if [ ! -f "README.md" ]; then
    echo "❌ 缺少: README.md"
    files_ok=false
fi

if [ "$files_ok" = false ]; then
    echo ""
    echo "❌ 文件检查失败，请确保所有文件都存在"
    exit 1
fi

echo "✅ 所有文件检查通过"
echo ""

# 询问GitHub仓库地址
echo "📝 请提供你的GitHub仓库信息："
echo ""
echo "如果你还没有创建仓库，请先："
echo "1. 访问 https://github.com/new"
echo "2. 创建一个名为 'smart-notification' 的仓库"
echo "3. 复制仓库地址（例如：https://github.com/你的用户名/smart-notification.git）"
echo ""
read -p "请输入你的GitHub仓库地址: " repo_url

if [ -z "$repo_url" ]; then
    echo "❌ 仓库地址不能为空"
    exit 1
fi

echo ""
echo "🔧 开始配置Git..."

# 初始化Git仓库
if [ ! -d ".git" ]; then
    git init
    echo "✅ Git仓库已初始化"
else
    echo "✅ Git仓库已存在"
fi

# 添加远程仓库
git remote remove origin 2>/dev/null
git remote add origin "$repo_url"
echo "✅ 远程仓库已配置: $repo_url"

# 添加文件
echo ""
echo "📦 添加文件到Git..."
git add .
echo "✅ 文件已添加"

# 提交
echo ""
echo "💾 提交更改..."
git commit -m "Initial commit: 智能通知系统"
echo "✅ 更改已提交"

# 推送
echo ""
echo "🚀 推送到GitHub..."
git branch -M main
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 部署成功！"
    echo ""
    echo "📋 下一步："
    echo "1. 访问你的GitHub仓库"
    echo "2. 进入 Settings → Secrets and variables → Actions"
    echo "3. 添加以下3个Secrets："
    echo "   - NOTION_API_TOKEN"
    echo "   - NOTION_DATABASE_ID"
    echo "   - FEISHU_WEBHOOK_URL"
    echo "4. 进入 Actions 页面，手动测试运行"
    echo ""
    echo "📖 详细配置步骤请查看: SETUP_GUIDE.md"
    echo ""
    echo "✅ 部署完成！"
else
    echo ""
    echo "❌ 推送失败，请检查："
    echo "1. 仓库地址是否正确"
    echo "2. 是否有权限推送"
    echo "3. GitHub认证是否配置正确"
    echo ""
    echo "💡 你也可以手动推送："
    echo "   git push -u origin main"
fi
