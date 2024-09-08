#/sentnel/gradio_server.py
import gradio as gr

from datetime import datetime,date,timedelta
from report_generator import ReportGenerator
from sentinel.services.subscription_service import SubscriptionService
from sentinel.logger import LOG
from sentinel.utils.github_api import GitHubAPI

report_generator = ReportGenerator()
subscription_manager = SubscriptionService()
github_api=GitHubAPI()

def export_progress_by_date_range(repo, days):
    raw_file_path = github_api.export_to_markdown_by_date_range(repo, days)
    report, report_file_path = report_generator.generate_formal_report(raw_file_path)

    return report, report_file_path

demo = gr.Interface(
    fn=export_progress_by_date_range,
    title="GitHubSentinel",
    inputs=[
        gr.Dropdown(
            subscription_manager.list_subscriptions(), label="订阅列表", info="已订阅GitHub项目"
        ),
        gr.Slider(value=2, minimum=1, maximum=7, step=1, label="报告周期", info="生成项目过去一段时间进展，单位：天"),

    ],
    outputs=[gr.Markdown(), gr.File(label="下载报告")],
)

if __name__ == "__main__":
    demo.launch(share=True, server_name="0.0.0.0")
    # demo.launch(share=True, server_name="0.0.0.0", auth=("django", "1234"))