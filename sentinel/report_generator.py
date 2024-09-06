# sentinel/report_generator.py

import os
from sentinel.llm_module import LLMModule
from sentinel.logger import LOG  # 导入日志模块，用于记录日志信息

class ReportGenerator:
    def __init__(self):
        self.llm = LLMModule()

    def generate_formal_report(self, markdown_file_path):
        # 读取Markdown文件并使用LLM生成日报
        with open(markdown_file_path, 'r') as file:
            markdown_content = file.read()

        report = self.llm.generate_summary(markdown_content)  # 调用LLM生成报告

        report_file_path = os.path.splitext(markdown_file_path)[0] + "_report.md"
        with open(report_file_path, 'w+') as report_file:
            report_file.write(report)  # 写入生成的报告

        LOG.info(f"GitHub 项目报告已保存到 {report_file_path}")

        return report, report_file_path

    def generate_formal_reports(self):
        daily_reports_dir = 'daily_progress'
        for filename in os.listdir(daily_reports_dir):
            if filename.endswith('.md') and not filename.endswith('_report.md'):
                filepath = os.path.join(daily_reports_dir, filename)
                self.generate_formal_report(filepath)

if __name__ == "__main__":
    report_generator = ReportGenerator()
    report_generator.generate_formal_reports()
