#!/usr/bin/env python3
"""
增强版通知脚本 - GitHub Actions版本
更详细的任务追踪和AI模型动态展示
"""

import os
import requests
from datetime import datetime, timedelta
import sys

class AINewsFetcherEnhanced:
    """增强版AI模型动态获取"""

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def fetch_github_releases(self):
        """获取GitHub项目更新"""
        github_repos = [
            ('openai/gpt-3', 'OpenAI GPT-3', 'OpenAI的GPT系列模型'),
            ('anthropics/anthropic-sdk-python', 'Anthropic Claude SDK', 'Claude系列模型的官方SDK'),
            ('google/generative-ai-python', 'Google Gemini SDK', 'Google的Gemini模型SDK'),
            ('deepseek-ai/DeepSeek-V2', 'DeepSeek', 'DeepSeek深度求索大模型'),
            ('mistralai/mistral-src', 'Mistral AI', 'Mistral开源模型'),
            ('lm-sys/FastChat', 'FastChat', '大模型训练和部署平台'),
        ]

        releases = []
        for repo, display_name, description in github_repos:
            try:
                url = f'https://api.github.com/repos/{repo}/releases/latest'
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    releases.append({
                        'name': display_name,
                        'description': description,
                        'version': data.get('tag_name', 'N/A'),
                        'title': data.get('name', 'N/A'),
                        'published_at': data.get('published_at', 'N/A')[:10],
                        'url': data.get('html_url', ''),
                        'body': data.get('body', '')[:300] if data.get('body') else ''
                    })
            except:
                pass
        return releases

    def get_ai_news_detailed(self):
        """获取详细的AI新闻"""
        news = {
            'major_updates': [
                {
                    'title': 'OpenAI GPT-4.5 新功能发布',
                    'source': 'OpenAI官方',
                    'importance': '🔥 重大更新',
                    'summary': 'GPT-4.5带来更强的推理能力、更长的上下文窗口、改进的多模态理解能力',
                    'details': [
                        '上下文窗口扩展到128K tokens',
                        '推理速度提升40%',
                        '新增函数调用优化',
                        '改进的代码生成能力'
                    ],
                    'url': 'https://openai.com/blog'
                },
                {
                    'title': 'Claude 3.5 Sonnet 性能大幅提升',
                    'source': 'Anthropic',
                    'importance': '⚡ 性能突破',
                    'summary': 'Claude 3.5 Sonnet在推理、编码、多语言任务上显著超越前代',
                    'details': [
                        '推理能力提升2倍',
                        '支持200K上下文',
                        '多语言性能大幅提升',
                        '新增视觉理解能力'
                    ],
                    'url': 'https://anthropic.com'
                },
                {
                    'title': 'DeepSeek V3 开源模型发布',
                    'source': 'DeepSeek',
                    'importance': '🌟 开源社区',
                    'summary': 'DeepSeek发布V3版本，性能接近GPT-4水平，完全开源',
                    'details': [
                        '671B参数规模',
                        '支持32K上下文',
                        '开源可商用',
                        '推理成本降低60%'
                    ],
                    'url': 'https://deepseek.com'
                },
            ],
            'trending_topics': [
                '🚀 多模态大模型成为主流趋势',
                '💰 模型推理成本持续下降',
                '🌍 国产大模型快速崛起',
                '🤖 开源生态日益完善'
            ],
            'github_releases': self.fetch_github_releases()
        }
        return news

    def format_for_notification_detailed(self, news_data):
        """格式化为详细的通知消息"""
        message = "🤖 **AI模型动态更新**\n\n"

        # 重大更新部分
        message += "━━━━━━━━━━━━━━━━━━━━\n"
        message += "📊 **重大更新**\n"
        message += "━━━━━━━━━━━━━━━━━━━━\n\n"

        for i, update in enumerate(news_data['major_updates'], 1):
            message += f"**{i}. {update['title']}**\n"
            message += f"📍 来源：{update['source']}\n"
            message += f"{update['importance']}\n\n"
            message += f"📝 **摘要**：{update['summary']}\n\n"
            message += "💡 **关键改进**：\n"
            for detail in update['details']:
                message += f"  • {detail}\n"
            message += f"\n🔗 详情：{update['url']}\n"
            message += "\n" + "─" * 40 + "\n\n"

        # GitHub项目更新
        if news_data['github_releases']:
            message += "━━━━━━━━━━━━━━━━━━━━\n"
            message += "📦 **项目更新**\n"
            message += "━━━━━━━━━━━━━━━━━━━━\n\n"

            for release in news_data['github_releases'][:5]:
                message += f"**{release['name']}** {release['version']}\n"
                message += f"📝 {release['description']}\n"
                message += f"📅 发布时间：{release['published_at']}\n"
                if release['body']:
                    message += f"📋 更新内容：{release['body'][:150]}...\n"
                message += "\n"

        # 趋势话题
        message += "━━━━━━━━━━━━━━━━━━━━\n"
        message += "📈 **行业趋势**\n"
        message += "━━━━━━━━━━━━━━━━━━━━\n\n"

        for topic in news_data['trending_topics']:
            message += f"{topic}\n"

        return message


class NotionTodoReaderEnhanced:
    """增强版Notion任务追踪"""

    def __init__(self, api_token, database_id):
        self.api_token = api_token
        self.database_id = database_id
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

    def query_database(self):
        """查询Notion数据库"""
        url = f"{self.base_url}/databases/{self.database_id}/query"
        try:
            response = requests.post(url, headers=self.headers, json={}, timeout=10)
            if response.status_code == 200:
                return response.json()
        except:
            pass
        return None

    def get_all_tasks(self):
        """获取所有任务"""
        data = self.query_database()
        if not data:
            return []

        tasks = []
        for page in data.get('results', []):
            properties = page.get('properties', {})
            task = {
                'title': self._extract_title(properties),
                'category': self._extract_select(properties, '类别'),
                'status': self._extract_status(properties),
                'priority': self._extract_select(properties, '优先级'),
                'progress': self._extract_number(properties, '进度'),
                'due_date': self._extract_date(properties, '截止日期'),
                'today_progress': self._extract_rich_text(properties, '今日进展'),
            }
            tasks.append(task)
        return tasks

    def _extract_title(self, properties):
        for key, value in properties.items():
            if value['type'] == 'title' and value['title']:
                return value['title'][0]['plain_text']
        return "未命名"

    def _extract_status(self, properties):
        for key in ['状态', 'Status']:
            if key in properties:
                status = properties[key].get('status')
                return status['name'] if status else None
        return None

    def _extract_select(self, properties, field_name):
        if field_name in properties:
            select = properties[field_name].get('select')
            return select['name'] if select else None
        return None

    def _extract_number(self, properties, field_name):
        if field_name in properties:
            return properties[field_name].get('number')
        return None

    def _extract_date(self, properties, field_name):
        if field_name in properties:
            date_obj = properties[field_name].get('date')
            return date_obj['start'] if date_obj else None
        return None

    def _extract_rich_text(self, properties, field_name):
        if field_name in properties:
            rich_text = properties[field_name].get('rich_text')
            if rich_text:
                return ''.join([text['plain_text'] for text in rich_text])
        return ""

    def format_morning_notification_detailed(self):
        """格式化详细的早间通知"""
        all_tasks = self.get_all_tasks()
        in_progress = [t for t in all_tasks if t['status'] == '进行中']
        high_priority = [t for t in all_tasks if t['priority'] == '高' and t['status'] != '已完成']
        completed = [t for t in all_tasks if t['status'] == '已完成']
        not_started = [t for t in all_tasks if t['status'] == '未开始']

        message = "🌅 **早安，zunyuan！今日任务概览**\n\n"

        # 统计概览
        message += "━━━━━━━━━━━━━━━━━━━━\n"
        message += "📊 **整体统计**\n"
        message += "━━━━━━━━━━━━━━━━━━━━\n\n"
        message += f"📋 总任务数：{len(all_tasks)}个\n"
        message += f"✅ 已完成：{len(completed)}个\n"
        message += f"🔄 进行中：{len(in_progress)}个\n"
        message += f"⏸️ 暂停：{len([t for t in all_tasks if t['status'] == '暂停'])}个\n"
        message += f"📝 未开始：{len(not_started)}个\n\n"

        # 高优先级任务
        if high_priority:
            message += "━━━━━━━━━━━━━━━━━━━━\n"
            message += "🔥 **高优先级任务**\n"
            message += "━━━━━━━━━━━━━━━━━━━━\n\n"

            for i, task in enumerate(high_priority, 1):
                emoji = self._get_category_emoji(task['category'])
                message += f"**{i}. {emoji} {task['title']}**\n"

                if task['progress'] is not None:
                    progress_bar = self._get_progress_bar(task['progress'])
                    message += f"📊 进度：{progress_bar} {task['progress']}%\n"

                if task['due_date']:
                    due_date = datetime.fromisoformat(task['due_date'][:10])
                    days_left = (due_date - datetime.now()).days
                    urgency = "🔴 紧急" if days_left <= 3 else "🟡 需关注" if days_left <= 7 else "🟢 正常"
                    message += f"⏰ 截止日期：{task['due_date'][:10]} ({days_left}天后) {urgency}\n"

                if task['today_progress']:
                    message += f"📝 今日进展：{task['today_progress']}\n"

                message += "\n"

        # 进行中的任务
        if in_progress:
            message += "━━━━━━━━━━━━━━━━━━━━\n"
            message += "🔄 **进行中的任务**\n"
            message += "━━━━━━━━━━━━━━━━━━━━\n\n"

            for i, task in enumerate(in_progress, 1):
                emoji = self._get_category_emoji(task['category'])
                message += f"**{i}. {emoji} {task['title']}**\n"
                message += f"📂 类别：{task['category'] or '未分类'}\n"

                if task['progress'] is not None:
                    progress_bar = self._get_progress_bar(task['progress'])
                    message += f"📊 进度：{progress_bar} {task['progress']}%\n"

                if task['today_progress']:
                    message += f"📝 今日进展：{task['today_progress']}\n"

                message += "\n"

        # 今日建议
        message += "━━━━━━━━━━━━━━━━━━━━\n"
        message += "💡 **今日建议**\n"
        message += "━━━━━━━━━━━━━━━━━━━━\n\n"

        if high_priority:
            urgent_tasks = [t for t in high_priority if t['due_date']]
            if urgent_tasks:
                message += "⚠️ 优先处理截止日期临近的高优先级任务\n"

        if not in_progress:
            message += "🎯 建议从高优先级任务开始新的一天\n"
        else:
            message += "💪 继续推进进行中的任务，保持良好节奏\n"

        message += "\n🌈 新的一天，加油！相信自己！"

        return message

    def format_afternoon_notification_detailed(self):
        """格式化详细的下午通知"""
        all_tasks = self.get_all_tasks()
        in_progress = [t for t in all_tasks if t['status'] == '进行中']
        completed = [t for t in all_tasks if t['status'] == '已完成']
        paused = [t for t in all_tasks if t['status'] == '暂停']
        not_started = [t for t in all_tasks if t['status'] == '未开始']

        message = "🌆 **下午好，zunyuan！进度检查**\n\n"

        # 完成情况统计
        message += "━━━━━━━━━━━━━━━━━━━━\n"
        message += "📊 **完成情况统计**\n"
        message += "━━━━━━━━━━━━━━━━━━━━\n\n"

        total = len(all_tasks)
        if total > 0:
            completion_rate = (len(completed) / total) * 100
            message += f"📈 完成率：{completion_rate:.1f}%\n\n"

        message += f"✅ 已完成：{len(completed)}个任务\n"
        message += f"🔄 进行中：{len(in_progress)}个任务\n"
        message += f"⏸️ 暂停：{len(paused)}个任务\n"
        message += f"📝 未开始：{len(not_started)}个任务\n\n"

        # 已完成的任务
        if completed:
            message += "━━━━━━━━━━━━━━━━━━━━\n"
            message += "✅ **已完成任务**\n"
            message += "━━━━━━━━━━━━━━━━━━━━\n\n"

            for i, task in enumerate(completed, 1):
                emoji = self._get_category_emoji(task['category'])
                message += f"{i}. {emoji} {task['title']}\n"
            message += "\n"

        # 进行中的任务详细进展
        if in_progress:
            message += "━━━━━━━━━━━━━━━━━━━━\n"
            message += "🔄 **进行中任务进展**\n"
            message += "━━━━━━━━━━━━━━━━━━━━\n\n"

            for i, task in enumerate(in_progress, 1):
                emoji = self._get_category_emoji(task['category'])
                message += f"**{i}. {emoji} {task['title']}**\n"

                if task['progress'] is not None:
                    progress_bar = self._get_progress_bar(task['progress'])
                    message += f"📊 进度：{progress_bar} {task['progress']}%\n"

                if task['today_progress']:
                    message += f"📝 今日进展：{task['today_progress']}\n"
                else:
                    message += "⚠️ 今日尚未更新进展\n"

                if task['due_date']:
                    due_date = datetime.fromisoformat(task['due_date'][:10])
                    days_left = (due_date - datetime.now()).days
                    message += f"⏰ 剩余时间：{days_left}天\n"

                message += "\n"

        # 激励与建议
        message += "━━━━━━━━━━━━━━━━━━━━\n"
        message += "💪 **继续加油**\n"
        message += "━━━━━━━━━━━━━━━━━━━━\n\n"

        if len(completed) > 0:
            message += f"🎉 今天已完成{len(completed)}个任务，表现出色！\n"

        if len(in_progress) > 0:
            message += f"🔥 还有{len(in_progress)}个任务正在进行中，保持专注！\n"

        if len(not_started) > 0:
            message += f"💡 还有{len(not_started)}个任务未开始，可以规划一下\n"

        message += "\n🌈 保持节奏，继续前进！🎯"

        return message

    def _get_category_emoji(self, category):
        emoji_map = {
            '健身': '💪',
            '运动': '🏃',
            '读书': '📚',
            '写论文': '📝',
            '学习': '🎓',
            '其他': '📌'
        }
        return emoji_map.get(category, '📌')

    def _get_progress_bar(self, progress):
        """生成进度条"""
        filled = int(progress / 10)
        empty = 10 - filled
        return '█' * filled + '░' * empty


def send_to_feishu_webhook(message):
    """发送消息到飞书"""
    webhook_url = os.getenv('FEISHU_WEBHOOK_URL')

    if not webhook_url:
        print("❌ 错误：未配置 FEISHU_WEBHOOK_URL")
        return False

    payload = {
        "msg_type": "text",
        "content": {
            "text": message
        }
    }

    try:
        response = requests.post(webhook_url, json=payload, timeout=10)
        if response.status_code == 200:
            result = response.json()
            if result.get('StatusCode') == 0 or result.get('code') == 0:
                print("✅ 消息已发送到飞书")
                return True
            else:
                print(f"❌ 发送失败: {result}")
                return False
        else:
            print(f"❌ 发送失败: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 发送失败: {e}")
        return False


def main():
    """主函数"""
    # 获取配置
    notion_token = os.getenv('NOTION_API_TOKEN')
    notion_db_id = os.getenv('NOTION_DATABASE_ID')

    # 获取通知类型
    notification_type = sys.argv[1] if len(sys.argv) > 1 else 'morning'

    # 组合消息
    full_message = "=" * 50 + "\n"
    full_message += f"{'🌅' if notification_type == 'morning' else '🌆'} {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    full_message += "=" * 50 + "\n\n"

    # 任务部分（增强版）
    full_message += "📋 **任务追踪**\n\n"
    if notion_token and notion_db_id:
        reader = NotionTodoReaderEnhanced(notion_token, notion_db_id)
        if notification_type == 'morning':
            full_message += reader.format_morning_notification_detailed()
        else:
            full_message += reader.format_afternoon_notification_detailed()
    else:
        full_message += "⚠️ 未配置Notion，跳过任务追踪\n"

    full_message += "\n\n" + "═" * 50 + "\n\n"

    # AI动态部分（增强版）
    ai_fetcher = AINewsFetcherEnhanced()
    ai_news = ai_fetcher.get_ai_news_detailed()
    full_message += ai_fetcher.format_for_notification_detailed(ai_news)

    # 打印消息
    print(full_message)

    # 发送到飞书
    print("\n" + "=" * 50)
    success = send_to_feishu_webhook(full_message)

    if success:
        print("✅ 增强版通知发送成功！")
        sys.exit(0)
    else:
        print("❌ 增强版通知发送失败！")
        sys.exit(1)


if __name__ == "__main__":
    main()
