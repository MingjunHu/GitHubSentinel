# GitHub Sentinel

**GitHub Sentinel** 是一款开源工具类 AI Agent，专为开发者和项目管理人员设计，能够定期（每日/每周）自动获取并汇总订阅的 GitHub 仓库最新动态。通过 Web UI 和命令行工具的支持，GitHub Sentinel 大大提高了团队协作效率和项目管理的便捷性。

## 功能概述

- **每日进展模块**：自动获取订阅仓库的 Issues、Pull Requests 和 Commits，生成项目进展报告并以 Markdown 格式导出。
- **LLM 模块**：集成了 OpenAI GPT-4 API，根据项目更新生成简明扼要的日报告。
- **Web UI 支持**：通过 Gradio 构建的 Web 界面，用户可以在线生成报告并下载。
- **调度器守护进程**：后台运行调度任务，定期检查仓库更新并生成报告。
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

### 2. 守护进程管理

GitHub Sentinel 支持以守护进程方式运行任务，通过 `daemon_control.sh` 脚本管理。以下是管理守护进程的常用命令：

- **启动守护进程**：

    ```bash
    ./daemon_control.sh start
    ```

- **停止守护进程**：

    ```bash
    ./daemon_control.sh stop
    ```

- **查看守护进程状态**：

    ```bash
    ./daemon_control.sh status
    ```

- **重启守护进程**：

    ```bash
    ./daemon_control.sh restart
    ```

### 3. Web UI 使用指南

GitHub Sentinel 通过 Gradio 提供了一个简单的 Web UI，用户可以在线生成报告并下载。

启动 Web UI：

```bash
python -m sentinel.gradio_server

Web 界面将自动启动并生成一个本地或在线的可访问链接，用户可以通过下拉菜单选择项目并生成报告。

配置文件
项目的主要配置项通过 sentinel/config.py 管理，可以通过修改以下参数来控制行为：

GITHUB_TOKEN：GitHub API 的访问令牌。
OPENAI_API_KEY：OpenAI 的 API 密钥，用于生成项目报告。
EMAIL_USERNAME 和 EMAIL_PASSWORD：用于发送报告通知邮件的邮箱账号和密码。
freq_days：定时任务的执行频率，默认为每天执行。
开发日志
v0.5: 完成报告生成功能，包括自动发送项目进展报告邮件。
v0.4.2: 添加守护进程控制脚本，支持后台运行任务并生成报告。
v0.4.1: 优化了调度器和命令行工具的管理，改进了日志记录。
v0.4: 集成了 Gradio Web UI，用户可以通过 Web 界面选择订阅项目并生成报告。
v0.3: 优化了 LLM 模块，完善了日志记录功能。
v0.2: 增加了每日进展报告的生成功能。
v0.1: 实现了 GitHub 仓库订阅功能并支持命令行工具。

贡献
欢迎提交问题和功能请求！如果你想贡献代码，请提交 Pull Request