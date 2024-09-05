# sentinel/report_generator.py

import os
from sentinel.llm_module import LLMModule

class ReportGenerator:
    def __init__(self):
        self.llm = LLMModule()

    def generate_formal_report(self, markdown_file):
        with open(markdown_file, 'r', encoding='utf-8') as file:
            content = file.read()

        summary = self.llm.generate_summary(content)
        report_filename = markdown_file.replace('.md', '_report.md')
        with open(report_filename, 'w', encoding='utf-8') as report_file:
            report_file.write(f"# Formal Daily Report\n\n{summary}")

        print(f"Generated formal report: {report_filename}")
        return report_filename

    def generate_formal_reports(self):
        daily_reports_dir = 'daily_reports'
        for filename in os.listdir(daily_reports_dir):
            if filename.endswith('.md') and not filename.endswith('_report.md'):
                filepath = os.path.join(daily_reports_dir, filename)
                self.generate_formal_report(filepath)

if __name__ == "__main__":
    report_generator = ReportGenerator()
    report_generator.generate_formal_reports()
