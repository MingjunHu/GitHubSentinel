# GitHub Sentinel

![GitHub stars](https://img.shields.io/github/stars/MingjunHu/GitHubSentinel?style=social)
![GitHub forks](https://img.shields.io/github/forks/MingjunHu/GitHubSentinel?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/MingjunHu/GitHubSentinel?style=social)
![GitHub repo size](https://img.shields.io/github/repo-size/MingjunHu/GitHubSentinel)
![GitHub language count](https://img.shields.io/github/languages/count/MingjunHu/GitHubSentinel)
![GitHub top language](https://img.shields.io/github/languages/top/MingjunHu/GitHubSentinel)
![GitHub last commit](https://img.shields.io/github/last-commit/MingjunHu/GitHubSentinel?color=red)


**GitHub Sentinel** 是一款开源工具类 AI Agent，专为开发者和项目管理人员设计，能够定期（每日/每周）自动获取并汇总订阅的 GitHub 仓库最新动态。通过 Web UI 和命令行工具的支持，GitHub Sentinel 大大提高了团队协作效率和项目管理的便捷性。

## 功能概述

- **订阅管理**：轻松管理和跟踪您关注的 GitHub 仓库。
- **更新检索**：自动检索并汇总订阅仓库的最新动态，包括提交记录、问题和拉取请求。
- **通知系统**：通过电子邮件等方式，实时通知订阅者项目的最新进展。
- **报告生成**：基于检索到的更新生成详细的项目进展报告，支持多种格式和模板，满足不同需求。
- **多模型支持**：结合 OpenAI 和 Ollama 模型，生成自然语言项目报告，提供更智能、精准的信息服务。
- **定时任务**：支持以守护进程方式执行定时任务，确保信息更新及时获取。
- **图形化界面**：基于 Gradio 实现了简单易用的 GUI 操作模式，降低使用门槛。
- **容器化**：项目支持 Docker 构建和容器化部署，便于在不同环境中快速部署和运行。
- **持续集成**：实现了完备的单元测试，便于进一步配置生产级 CI/CD 流程，确保项目的稳定性和高质量交付。

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

## 配置文件
项目的主要配置项通过 sentinel/config.py 管理，可以通过修改以下参数来控制行为：

GITHUB_TOKEN：GitHub API 的访问令牌。
OPENAI_API_KEY：OpenAI 的 API 密钥，用于生成项目报告。
EMAIL_USERNAME 和 EMAIL_PASSWORD：用于发送报告通知邮件的邮箱账号和密码。
freq_days：定时任务的执行频率，默认为每天执行。
exec_time：定时任务的执行时间，默认为每天 08:00。

## 使用 Docker 构建与验证

为了便于在各种环境中构建和部署 GitHub Sentinel 项目，我们提供了 Docker 支持。该支持包括以下文件和功能：

### 1. `Dockerfile`

#### 用途
`Dockerfile` 是用于定义如何构建 Docker 镜像的配置文件。它描述了镜像的构建步骤，包括安装依赖、复制项目文件、运行单元测试等。

#### 关键步骤
- 使用 `python:3.10-slim` 作为基础镜像，并设置工作目录为 `/app`。
- 复制项目的 `requirements.txt` 文件并安装 Python 依赖。
- 复制项目的所有文件到容器，并赋予 `validate_tests.sh` 脚本执行权限。
- 在构建过程中执行 `validate_tests.sh` 脚本，以确保所有单元测试通过。如果测试失败，构建过程将中止。
- 构建成功后，将默认运行 `src/main.py` 作为容器的入口点。

### 2. `build_image.sh`

#### 用途
`build_image.sh` 是一个用于自动构建 Docker 镜像的 Shell 脚本。它从当前的 Git 分支获取分支名称，并将其用作 Docker 镜像的标签，便于在不同分支上生成不同的 Docker 镜像。

#### 功能
- 获取当前的 Git 分支名称，并将其用作 Docker 镜像的标签。
- 使用 `docker build` 命令构建 Docker 镜像，并使用当前 Git 分支名称作为标签。

#### 使用示例
```bash
chmod +x build_image.sh
./build_image.sh

## 开发日志
v0.8.1已知bug处理
v0.8：容器化部署，gradio私有化大模型选择。
v0.6：增加LLM配置项，支持Ollama模型和Open AI模型
v0.5: 完成报告生成功能，包括自动发送项目进展报告邮件。
v0.4.2: 添加守护进程控制脚本，支持后台运行任务并生成报告。
v0.4.1: 优化了调度器和命令行工具的管理，改进了日志记录。
v0.4: 集成了 Gradio Web UI，用户可以通过 Web 界面选择订阅项目并生成报告。
v0.3: 优化了 LLM 模块，完善了日志记录功能。
v0.2: 增加了每日进展报告的生成功能。
v0.1: 实现了 GitHub 仓库订阅功能并支持命令行工具。

贡献
欢迎提交问题和功能请求！如果你想贡献代码，请提交 Pull Request。
