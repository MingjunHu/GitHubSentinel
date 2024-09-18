#/sentnel/gradio_server.py
import gradio as gr

from sentinel.config import Config
from datetime import datetime,date,timedelta
from sentinel.report_generator import ReportGenerator
from sentinel.services.subscription_service import SubscriptionService
from sentinel.logger import LOG
from sentinel.utils.github_api import GitHubAPI
from sentinel.llm_module import LLMModule
from sentinel.utils.hacker_news_api import HackerNewsClient

config = Config()
subscription_manager = SubscriptionService()
github_api=GitHubAPI()
hacker_news_client = HackerNewsClient() # 创建 Hacker News 客户端实例

def export_progress_by_date_range(model_type, model_name,repo, days):
    config.llm_model_type = model_type

    if model_type == "openai":
        config.openai_model_name = model_name
    else:
        config.ollama_model_name = model_name

    llm = LLMModule(config)  # 创建语言模型实例
    report_generator = ReportGenerator(llm, config.report_types)  # 创建报告生成器实例

    raw_file_path = github_api.export_to_markdown_by_date_range(repo, days)
    report, report_file_path = report_generator.generate_formal_report(raw_file_path)

    return report, report_file_path

def generate_hn_hour_topic(model_type, model_name):
    config.llm_model_type = model_type

    if model_type == "openai":
        config.openai_model_name = model_name
    else:
        config.ollama_model_name = model_name

    llm = LLMModule(config)  # 创建语言模型实例
    report_generator = ReportGenerator(llm, config.report_types)  # 创建报告生成器实例

    markdown_file_path = hacker_news_client.export_top_stories()
    report, report_file_path = report_generator.generate_hn_topic_report(markdown_file_path)

    return report, report_file_path  # 返回报告内容和报告文件路径


# 定义一个回调函数，用于根据 Radio 组件的选择返回不同的 Dropdown 选项
def update_model_list(model_type):
    if model_type == "openai":
        return gr.Dropdown(choices=["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"], label="选择模型")
    elif model_type == "ollama":
        return gr.Dropdown(choices=["glm4", "gemma2:2b", "qwen2:7b"], label="选择模型")

# 创建 Gradio 界面
with gr.Blocks(title="GitHubSentinel") as demo:
    # 创建 GitHub 项目进展 Tab
    with gr.Tab("GitHub 项目进展"):
        gr.Markdown("## GitHub 项目进展")  # 添加小标题

        # 创建 Radio 组件
        model_type = gr.Radio(["openai", "ollama"], label="模型类型", info="使用 OpenAI GPT API 或 Ollama 私有化模型服务")

        # 创建 Dropdown 组件
        model_name = gr.Dropdown(choices=["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"], label="选择模型")

        # 创建订阅列表的 Dropdown 组件
        subscription_list = gr.Dropdown(subscription_manager.list_subscriptions(), label="订阅列表", info="已订阅GitHub项目")

        # 创建 Slider 组件
        days = gr.Slider(value=2, minimum=1, maximum=7, step=1, label="报告周期", info="生成项目过去一段时间进展，单位：天")

        # 使用 radio 组件的值来更新 dropdown 组件的选项
        model_type.change(fn=update_model_list, inputs=model_type, outputs=model_name)

        # 创建按钮来生成报告
        button = gr.Button("生成报告")

        # 设置输出组件
        markdown_output = gr.Markdown()
        file_output = gr.File(label="下载报告")

        # 将按钮点击事件与导出函数绑定
        button.click(export_progress_by_date_range, inputs=[model_type, model_name, subscription_list, days], outputs=[markdown_output, file_output])

    # 创建 Hacker News 热点话题 Tab
    with gr.Tab("Hacker News 热点话题"):
        gr.Markdown("## Hacker News 热点话题")  # 添加小标题

        # 创建 Radio 组件
        model_type = gr.Radio(["openai", "ollama"], label="模型类型", info="使用 OpenAI GPT API 或 Ollama 私有化模型服务")

        # 创建 Dropdown 组件
        model_name = gr.Dropdown(choices=["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"], label="选择模型")

        # 使用 radio 组件的值来更新 dropdown 组件的选项
        model_type.change(fn=update_model_list, inputs=model_type, outputs=model_name)

        # 创建按钮来生成报告
        button = gr.Button("生成最新热点话题")

        # 设置输出组件
        markdown_output = gr.Markdown()
        file_output = gr.File(label="下载报告")

        # 将按钮点击事件与导出函数绑定
        button.click(generate_hn_hour_topic, inputs=[model_type, model_name,], outputs=[markdown_output, file_output])

if __name__ == "__main__":
    demo.launch(share=True, server_name="0.0.0.0",server_port=8888)
    # demo.launch(share=True, server_name="0.0.0.0", auth=("django", "1234"))