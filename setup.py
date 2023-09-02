from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="network-scanner",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A network scanner for scanning IP addresses and open ports.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/network-scanner",
    packages=find_packages(),
    install_requires=[
        "requests==2.26.0",
        "psutil==5.8.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
