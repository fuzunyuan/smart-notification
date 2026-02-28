# GitHub Actions 配置指南

## 📋 配置步骤

### 第1步：创建GitHub仓库

#### 方法1：创建新仓库（推荐）

1. 访问 https://github.com/new
2. 填写信息：
   - **Repository name**: `smart-notification`
   - **Description**: `智能通知系统`
   - **Visibility**: Public（公开）或 Private（私有）
3. 点击 `Create repository`

#### 方法2：使用现有仓库

如果你想用现有仓库，跳过这一步。

---

### 第2步：上传代码

#### 方式A：通过网页上传（最简单）

1. 在你的仓库页面，点击 `Add file` → `Upload files`
2. 按照以下结构创建文件夹和文件：

```
.github/
  workflows/
    notification.yml    ← 上传这个文件
scripts/
  notification.py        ← 上传这个文件
README.md                ← 上传这个文件
```

3. 在底部填写提交信息：`Initial commit: 智能通知系统`
4. 点击 `Commit changes`

#### 方式B：通过Git命令行

```bash
# 进入本地目录
cd ~/.openclaw/workspace/github-actions-notification

# 初始化Git仓库
git init

# 添加远程仓库（替换成你的仓库地址）
git remote add origin https://github.com/你的用户名/smart-notification.git

# 添加文件
git add .

# 提交
git commit -m "Initial commit: 智能通知系统"

# 推送到GitHub
git branch -M main
git push -u origin main
```

---

### 第3步：配置Secrets

**这是最重要的一步！** 🔑

1. 进入你的仓库页面
2. 点击 `Settings` 标签
3. 在左侧菜单找到 `Secrets and variables` → `Actions`
4. 点击 `New repository secret`

#### 需要添加的3个Secrets：

**Secret 1: NOTION_API_TOKEN**
```
Name: NOTION_API_TOKEN
Value: 你的Notion API Token（格式：ntn_xxxxx）
```
点击 `Add secret`

**Secret 2: NOTION_DATABASE_ID**
```
Name: NOTION_DATABASE_ID
Value: 你的数据库ID（32位字符串）
```
点击 `Add secret`

**Secret 3: FEISHU_WEBHOOK_URL**
```
Name: FEISHU_WEBHOOK_URL
Value: 你的飞书Webhook URL
```
点击 `Add secret`

✅ 完成后，你应该看到3个secrets已配置。

---

### 第4步：启用GitHub Actions

1. 点击 `Actions` 标签
2. 如果看到黄色提示框，点击 `I understand my workflows, go ahead and enable them`
3. 你应该看到 `Daily Notification` 工作流

---

### 第5步：测试运行

**手动触发测试：**

1. 在 `Actions` 页面，点击 `Daily Notification`
2. 点击右侧的 `Run workflow` 按钮
3. 在下拉菜单中：
   - `Notification type`: 选择 `morning`
4. 点击绿色的 `Run workflow` 按钮

**查看运行结果：**

1. 等待几秒钟，刷新页面
2. 点击最新运行的工作流（黄色圆点表示正在运行）
3. 展开各个步骤查看日志
4. 确认看到 `✅ 消息已发送到飞书`

**检查飞书：**

打开你的飞书群，应该看到测试通知了！🎉

---

### 第6步：等待定时通知

配置完成！系统会在每天自动运行：

- 🌅 **北京时间 10:00** - 早间通知
- 🌆 **北京时间 16:00** - 下午通知

**注意：** GitHub Actions的定时任务可能有几分钟延迟，这是正常的。

---

## 🔧 高级配置

### 修改通知时间

编辑 `.github/workflows/notification.yml`：

```yaml
on:
  schedule:
    - cron: '0 2 * * *'  # 早间通知（UTC时间）
    - cron: '0 8 * * *'  # 下午通知（UTC时间）
```

**时区转换表（北京时间 → UTC）：**

| 北京时间 | UTC时间 | Cron表达式 |
|---------|---------|-----------|
| 09:00   | 01:00   | `0 1 * * *` |
| 10:00   | 02:00   | `0 2 * * *` |
| 11:00   | 03:00   | `0 3 * * *` |
| 16:00   | 08:00   | `0 8 * * *` |
| 17:00   | 09:00   | `0 9 * * *` |
| 18:00   | 10:00   | `0 10 * * *` |

修改后需要提交更改：

```bash
git add .github/workflows/notification.yml
git commit -m "Update notification time"
git push
```

### 禁用某个通知

如果你想只保留一个通知时间，编辑workflow文件，删除不需要的 `cron` 行。

---

## 🐛 故障排查

### 问题1：Actions没有运行

**可能原因：**
- 仓库刚创建，需要等待
- Actions未启用

**解决方法：**
1. 确认已在Actions页面启用工作流
2. 尝试手动触发测试
3. 等待几分钟后再检查

### 问题2：通知发送失败

**检查步骤：**
1. 进入Actions页面，查看运行日志
2. 检查Secrets是否配置正确
3. 确认飞书Webhook URL有效

**常见错误：**
- `❌ 错误：未配置 FEISHU_WEBHOOK_URL` → Secrets配置错误
- `❌ 发送失败: HTTP 400` → Webhook URL无效
- `查询失败: 401` → Notion Token错误

### 问题3：Notion任务读取失败

**检查步骤：**
1. 确认 `NOTION_API_TOKEN` 正确
2. 确认 `NOTION_DATABASE_ID` 正确（32位字符串）
3. 确认数据库已授权integration访问

---

## 💡 提示

### 查看运行历史

在 `Actions` 页面可以看到所有运行历史，包括：
- 运行时间
- 运行状态（成功/失败）
- 详细日志

### 接收通知

GitHub会在工作流失败时发送邮件通知。如果需要，可以配置：
1. 进入仓库 `Settings` → `Notifications`
2. 配置邮件通知规则

### 节省资源

如果不需要Notion功能，可以在 `notification.py` 中注释掉Notion相关代码，只保留AI动态部分。

---

## ✅ 配置完成检查清单

- [ ] 创建GitHub仓库
- [ ] 上传代码文件
- [ ] 配置3个Secrets
  - [ ] NOTION_API_TOKEN
  - [ ] NOTION_DATABASE_ID
  - [ ] FEISHU_WEBHOOK_URL
- [ ] 启用GitHub Actions
- [ ] 手动测试运行成功
- [ ] 飞书群收到测试通知
- [ ] 等待定时通知

---

## 🎉 完成！

配置完成后，你的智能通知系统就上线了！

从现在开始，每天10:00和16:00，你都会自动收到任务追踪和AI动态通知！

**享受你的智能助手吧！** 🚀
