# sentinel/llm_module.py
from openai import OpenAI
import os
from sentinel.config import Config

class LLMModule:
    def __init__(self):
        # 从配置项中获取 OpenAI API 密钥
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)

    def generate_summary(self, markdown_content,dry_run=False):
        # 调用 OpenAI GPT-4 API，生成报告
        prompt = f"以下是项目的最新进展，根据功能合并同类项，形成一份简报，至少包含：1）新增功能；2）主要改进；3）修复问题；:\n\n{markdown_content}"
        sys_prompt=f"你接下来收到的都是开源项目的最新进展。你根据进展，总结成一个中文的报告，以 项目名称和日期 开头，包含：新增功能、主要改进，修复问题等章节。"
        if dry_run:
            with open("daily_progress/prompt.txt", "w+") as f:
                f.write(prompt)
            return "DRY RUN"

        print("Before call GPT")
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
                {"role": "system","content": sys_prompt},
            ]
        )
        print("After call GPT")
        print(response)
        return response.choices[0].message.content


