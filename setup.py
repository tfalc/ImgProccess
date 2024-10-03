from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()


with open("requirements.txt") as req:
    requirements = req.read().splitlines()


setup(
    name="img_processing",
    version="1.0.0",
    author="Thiago Falcão",
    author_email="n/a",
    description="Processador de imagens",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tfalc/ImgProccess.git",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',)