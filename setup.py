from pathlib import Path

from setuptools import find_packages
from setuptools import setup


setup(
    name="JFrog Audit",
    packages=find_packages(exclude=(["test*", "tmp*"])),
    description="Audit code before commit",
    author="JFrog",
    author_email="marcelol@jfrog.com",
    url="https://github.com/marcelonyc/jfrog-pre-commit",
    keywords=["jfrog-audit", "pre-commit", "jas"],
    entry_points={
        "console_scripts": [
            "jfrog-audit = python_projects.src.main:main",
        ],
    },
)
