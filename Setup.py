from setuptools import setup, find_packages

setup(
    name="WebGenie",
    version="0.1.0",
    author="Nitin Kumar Sharma",
    author_email="your_email@example.com",  # Replace with your email
    description="A CLI tool to create basic web development project structure with boilerplate code.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/webproject-cli",  # Replace with your GitHub repo link
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "WebGenie=WebGenie._main_:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)