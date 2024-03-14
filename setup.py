from pathlib import Path
from setuptools import find_packages
from setuptools import setup


def get_version():
    """Parse package __version__.py to get version."""
    versionpy = (Path("python_projects/src") / "__version__.py").read_text()
    version = versionpy.split("=")[1].strip().strip('"')
    return version


VERSION = get_version()


setup(
    name="JFrog Audit",
    packages=find_packages(exclude=(["test*", "tmp*"])),
    description="Audit code before commit",
    version=VERSION,
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
