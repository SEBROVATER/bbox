from setuptools import setup, find_packages


with open("README.md", "r") as file:
    long_desc = file.read()

setup(
    name="bbox",
    version="0.1.0",
    author="Konstantin Sebrovskiy",
    author_email="sebrovskiy.k@gmail.com",
    description="Objected management of bboxes",
    url="https://github.com/SEBROVATER/bbox",
    license="MIT",
    packages=find_packages(),
    long_description=long_desc,
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
)
