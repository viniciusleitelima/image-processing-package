from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_vll",
    version="0.0.1",
    author="Vinicius Lima",
    author_email="viniciusleite.desenvolvedor@gmail.com",
    description="image processing",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/viniciusleitelima/image-processing-package",
    package=find_packages(),
    install_requirements=requirements,
    python_requires=">=3.8"
)        