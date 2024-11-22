from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="env-json-converter",  # Package name
    version="1.0.0",  # Version of the package
    author="Paul Isaris",
    author_email="paulisaris@gmail.com",
    description="A secure tool to convert between .env and JSON file formats locally.",
    long_description="**Env-JSON Converter** is a simple and secure Python package that allows you to convert `.env` files to JSON and vice versa. Unlike online tools, this package ensures your sensitive information (like API keys and secrets) remains private and secure by running entirely on your local machine. The package is easy to use and can be run from the command line. It is ideal for developers who need to convert between these two formats quickly and securely.",
    long_description_content_type="text/markdown",  # Format of the long description
    url="https://github.com/PavlosIsaris/env-json-converter",  # Project homepage
    project_urls={
        "Bug Tracker": "https://github.com/PavlosIsaris/env-json-converter/issues",
        "Documentation": "https://github.com/PavlosIsaris/env-json-converter#readme",
    },
    license="MIT",  # License type
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    packages=find_packages(where="."),  # Automatically find all packages
    python_requires=">=3.7",  # Minimum Python version
    entry_points={
        "console_scripts": [
            "env-json=converter.env_json_converter:main",  # Create CLI command
        ],
    },
    install_requires=[],  # List of dependencies (empty if none are required)
    include_package_data=True,  # Include other files specified in MANIFEST.in
)
