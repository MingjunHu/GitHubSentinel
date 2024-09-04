from setuptools import setup, find_packages

setup(
    name='GitHubSentinel',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'gh-sentinel=sentinel.cli.sentinel_cli:main',  # 简短命令 gh-sentinel
        ],
    },
)
