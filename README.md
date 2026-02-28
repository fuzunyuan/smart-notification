# 🤖 zunyuan的智能通知系统

基于GitHub Actions的智能通知系统，每天定时发送任务追踪和AI模型动态到飞书。

## ✨ 功能特点

- ✅ **完全免费** - 使用GitHub Actions，无需服务器
- ✅ **稳定可靠** - GitHub自动运行，24/7不间断
- ✅ **双重提醒** - 每天早10:00和下午16:00
- ✅ **内容丰富** - Notion任务追踪 + AI模型动态
- ✅ **易于维护** - 代码开源，随时调整

## 📋 通知内容

### 早间通知（10:00）
- 🌅 今日任务概览
- ⚠️ 高优先级任务提醒
- 🤖 AI模型动态更新

### 下午通知（16:00）
- 🌆 进度检查
- 📊 完成情况统计
- 🤖 AI最新要闻

## 🚀 快速开始

### 1. Fork这个仓库

点击右上角 `Fork` 按钮，将仓库复制到你的账号下。

### 2. 配置Secrets

进入你fork的仓库，依次点击：

```
Settings → Secrets and variables → Actions → New repository secret
```

添加以下3个secrets：

| Name | Value | 说明 |
|------|-------|------|
| `NOTION_API_TOKEN` | `ntn_xxxxx` | Notion API Token |
| `NOTION_DATABASE_ID` | `32位ID` | Notion数据库ID |
| `FEISHU_WEBHOOK_URL` | `https://...` | 飞书Webhook URL |

### 3. 启用GitHub Actions

进入 `Actions` 标签页，如果看到提示，点击 `I understand my workflows, go ahead and enable them`

### 4. 测试运行

在 `Actions` 页面：
1. 选择 `Daily Notification` 工作流
2. 点击 `Run workflow`
3. 选择 `morning` 或 `afternoon`
4. 点击 `Run workflow` 按钮

查看运行日志，确认通知已发送。

### 5. 等待定时通知

配置完成后，系统会在每天：
- 🌅 **10:00** - 早间通知
- 🌆 **16:00** - 下午通知

自动发送到你的飞书群！

## 📁 项目结构

```
.
├── .github/
│   └── workflows/
│       └── notification.yml    # GitHub Actions工作流
├── scripts/
│   └── notification.py          # 通知脚本
└── README.md                    # 本文件
```

## 🔧 自定义配置

### 修改通知时间

编辑 `.github/workflows/notification.yml`：

```yaml
on:
  schedule:
    - cron: '0 2 * * *'  # 修改这里（UTC时间）
    - cron: '0 8 * * *'  # 修改这里（UTC时间）
```

**时区转换（北京时间 → UTC）：**
- 北京时间 10:00 = UTC 02:00
- 北京时间 16:00 = UTC 08:00
- 北京时间 09:00 = UTC 01:00

### 添加更多AI信息源

编辑 `scripts/notification.py` 中的 `AINewsFetcher` 类，添加新的数据源。

### 调整通知格式

编辑 `scripts/notification.py` 中的格式化函数。

## 📊 监控和调试

### 查看运行日志

1. 进入 `Actions` 页面
2. 点击具体的工作流运行
3. 查看各个步骤的日志

### 常见问题

**Q: 没有收到通知？**
- 检查Secrets是否配置正确
- 查看Actions运行日志
- 确认飞书Webhook URL有效

**Q: Notion任务读取失败？**
- 检查NOTION_API_TOKEN和NOTION_DATABASE_ID
- 确认数据库已授权integration访问

**Q: 想临时发送通知？**
- 使用 `workflow_dispatch` 手动触发
- 选择 `morning` 或 `afternoon`

## 🛡️ 安全说明

- ✅ 所有敏感信息存储在GitHub Secrets中
- ✅ 代码中不包含任何密钥或token
- ✅ Notion和飞书API调用都是只读操作
- ✅ 不会泄露任何隐私数据

## 📝 更新日志

### v1.0.0 (2026-02-28)
- ✅ 初始版本
- ✅ 支持Notion任务追踪
- ✅ 支持AI模型动态
- ✅ 飞书Webhook通知
- ✅ 定时任务（10:00 + 16:00）

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License

---

**享受你的智能通知系统！** 🎉
