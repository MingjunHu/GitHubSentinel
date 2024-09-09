# GitHub Sentinel

**GitHub Sentinel** 是一款开源工具类 AI Agent，专为开发者和项目管理人员设计，能够定期（每日/每周）自动获取并汇总订阅的 GitHub 仓库最新动态。通过 Web UI 和命令行工具的支持，GitHub Sentinel 大大提高了团队协作效率和项目管理的便捷性。

## 功能概述

- **每日进展模块**：自动获取订阅仓库的 Issues、Pull Requests 和 Commits，生成项目进展报告并以 Markdown 格式导出。
- **LLM 模块**：集成了 OpenAI GPT-4 API，根据项目更新生成简明扼要的日报告。
- **Web UI 支持**：通过 Gradio 构建的 Web 界面，用户可以在线生成报告并下载。
- **日志记录**：通过 Loguru 提供详细的日志记录，确保项目运行的透明性和可调试性。

## 安装

### 环境要求

- Python 3.6+
- Git

### 安装步骤

1. 克隆项目到本地：

    ```bash
    git clone https://github.com/yourusername/GitHubSentinel.git
    cd GitHubSentinel
    ```

2. 安装依赖：

    ```bash
    pip install .
    ```

3. 配置环境变量（可选，推荐使用 `.env` 文件）：

    ```bash
    export GITHUB_TOKEN='your_github_token'
    export OPENAI_API_KEY='your_openai_api_key'
    export EMAIL_USERNAME='your_email@example.com'
    export EMAIL_PASSWORD='your_email_password'
    export SMTP_SERVER='your_smtp_server'
    export SMTP_PORT='465'
    ```

## 使用指南

### 1. 命令行工具

GitHub Sentinel 提供了一个便捷的命令行工具 `gh-sentinel`，支持以下功能：

- **生成每日进展报告**：

    ```bash
    gh-sentinel progress
    ```

- **生成项目报告**：

    ```bash
    gh-sentinel report
    ```

- **启动后台调度器**：

    ```bash
    gh-sentinel start-scheduler
    ```

- **停止后台调度器**：

    ```bash
    gh-sentinel stop-scheduler
    ```

- **添加订阅仓库**：

    ```bash
    gh-sentinel add <repository>
    ```

- **移除订阅仓库**：

    ```bash
    gh-sentinel remove <repository>
    ```

- **列出所有订阅仓库**：

    ```bash
    gh-sentinel list
    ```

### 2. Web UI 使用指南

GitHub Sentinel 通过 Gradio 提供了一个简单的 Web UI，用户可以在线生成报告并下载。

启动 Web UI：

```bash
python -m sentinel.gradio_server
