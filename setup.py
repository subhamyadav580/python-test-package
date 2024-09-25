from setuptools import setup, find_packages

setup(
    name="sum_num",  # Replace with your package name
    version="0.1.2",
    author="Shubham Yadav",
    author_email="subhamyadav580@gmail.com",
    description="A package for addition and multiplication",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/subhamyadav580/python-test-package",  # Replace with your GitHub URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Use your license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
