# ⚡ 快速配置指南（5分钟完成）

## 🎯 目标

配置GitHub Actions，实现每天10:00和16:00自动发送通知到飞书。

---

## 📋 你需要的信息

你需要准备以下3个信息：

```
1. Notion API Token - 格式：ntn_xxxxx
2. Notion Database ID - 格式：32位字符串
3. 飞书 Webhook URL - 格式：https://open.feishu.cn/open-apis/bot/v2/hook/xxxxx
```

**如何获取这些信息请查看 `GET_FEISHU_ID.md` 和飞书开放平台文档。**

---

## 🚀 5步完成配置

### 第1步：创建GitHub仓库（1分钟）

1. 访问：https://github.com/new
2. Repository name: `smart-notification`
3. 选择 Public 或 Private
4. 点击 `Create repository`

### 第2步：上传代码（2分钟）

**方式A：网页上传（最简单）**

1. 在你的新仓库页面，点击 `uploading an existing file`
2. 打开本地目录：`~/.openclaw/workspace/github-actions-notification/`
3. 拖拽以下文件到网页：
   - `.github` 文件夹（包含workflows/notification.yml）
   - `scripts` 文件夹（包含notification.py）
   - `README.md`
   - `.gitignore`
4. 点击 `Commit changes`

**方式B：使用Git命令**

```bash
cd ~/.openclaw/workspace/github-actions-notification
bash scripts/deploy.sh
```

### 第3步：配置Secrets（1分钟）

1. 进入仓库，点击 `Settings`
2. 左侧菜单：`Secrets and variables` → `Actions`
3. 点击 `New repository secret`，添加3个：

**Secret 1:**
```
Name: NOTION_API_TOKEN
Value: 你的Notion API Token
```

**Secret 2:**
```
Name: NOTION_DATABASE_ID
Value: 你的Notion Database ID
```

**Secret 3:**
```
Name: FEISHU_WEBHOOK_URL
Value: 你的飞书Webhook URL
```

### 第4步：启用Actions（30秒）

1. 点击 `Actions` 标签
2. 点击 `I understand my workflows, go ahead and enable them`

### 第5步：测试运行（30秒）

1. 在 `Actions` 页面，点击 `Daily Notification`
2. 点击 `Run workflow` → 选择 `morning` → `Run workflow`
3. 等待运行完成
4. 检查飞书群是否收到通知

---

## ✅ 完成！

配置完成后，系统会在每天：
- 🌅 **10:00** - 早间通知
- 🌆 **16:00** - 下午通知

自动发送到你的飞书群！

---

## 📞 需要帮助？

查看详细文档：
- `SETUP_GUIDE.md` - 完整配置指南
- `README.md` - 项目说明

---

## 🎉 恭喜！

你的智能通知系统即将上线！
