from setuptools import setup, find_packages

setup(
    name='GitHubSentinel',
    version='0.8',  # 更新为v0.8.0版本
    packages=find_packages(),
    install_requires=[
        'requests',
        'openai',
        'loguru',
        'gradio',  # 添加gradio依赖
        'python-daemon',  # 新增 python-daemon 依赖
        'datetime',
        'schedule',
        'markdown2',
    ],
    entry_points={
        'console_scripts': [
            'gh-sentinel=sentinel.cli.sentinel_cli:main',  # 注册命令行工具
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
