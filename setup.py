"""Setup configuration for the practice project."""
from setuptools import setup, find_packages

setup(
    name="practice-project",
    version="0.1.0",
    description="A practice repository for testing GitHub automations",
    author="Practice Team",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
        "flask>=2.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "practice-cli=practice.cli:main",
        ],
    },
)
