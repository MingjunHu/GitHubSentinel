from setuptools import setup, find_packages

setup(
    name='GitHubSentinel',
    version='0.3.2',  # 更新为最新的版本号
    packages=find_packages(),
    install_requires=[
        'requests',
        'openai',
        'loguru',
    ],
    entry_points={
        'console_scripts': [
            'gh-sentinel=sentinel.cli.sentinel_cli:main',  # 注册为命令行工具
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)