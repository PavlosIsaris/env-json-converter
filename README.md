# Env-JSON Converter 🛠️🔄

**Env-JSON Converter** is a simple and secure Python package that allows you to convert `.env` files to JSON and vice
versa. Unlike online tools, this package ensures your sensitive information (like API keys and secrets) remains private
and secure by running entirely on your local machine.

---

## Why Use Env-JSON Converter? 🤔

### 🔒 **Privacy and Security**

Online tools like [JSONFormatter.org](https://jsonformatter.org/) require you to paste your `.env` files online, which
can expose sensitive information. With Env-JSON Converter, everything happens locally, ensuring your data remains
secure.

### ⚡ **Fast and Lightweight**

The package is simple to use and does not depend on any heavy external libraries.

### 📦 **Reusable and Extensible**

You can integrate this package into your projects or use it as a standalone CLI tool.

---

## Features 🌟

- **Convert `.env` to JSON:** Transform environment variable files into structured JSON.
- **Convert JSON to `.env`:** Generate `.env` files from JSON, making it easy to switch formats.
- **Secure by Design:** Runs entirely on your local machine, with no risk of data leakage.
- **Open Source:** Contribute, audit, or extend the code to suit your needs.

---

## Alternatives and Their Limitations 🚧

### JSONFormatter.org

While tools like [JSONFormatter.org](https://jsonformatter.org/) are convenient, they require uploading your `.env` file
online.
This poses a significant **security risk**, especially when handling sensitive information such as:

* API keys
* Database credentials
* Secrets for third-party integrations

Env-JSON Converter ensures your data never leaves your local environment, making it the safer choice for developers and
teams prioritizing security.

Start using Env-JSON Converter today and enjoy secure, fast, and easy file format conversion! 💪

---

## Installation 🚀

This package contains a `setup.sh` script that creates a virtual environment and installs the package. Follow these
steps:

```bash
git clone https://github.com/PavlosIsaris/env-json-converter.git

cd env-json-converter

chmod +x setup.sh

./setup.sh
```

## Usage 🖥️

### CLI Usage

After installation, you can use the `env-json` command:

#### Convert .env to JSON

```bash
env-json env-to-json /path/to/your/.env /path/to/save/output.json
```

#### Convert JSON to .env

```bash
env-json json-to-env /path/to/your.json /path/to/save/output.env
```

#### As a Python Library

You can also use the package in your Python code:

```bash
from converter.env_json_converter import env_to_json, json_to_env

# Convert .env to JSON
env_to_json('/path/to/.env', '/path/to/output.json')

# Convert JSON to .env
json_to_env('/path/to/input.json', '/path/to/output.env')
```

## Testing 🧪

Run the included unit tests to verify the package works as expected:

```bash
pytest tests/
```

## Development 🛠️

### Project Structure

The project is structured as follows:

```bash
env-json-converter/
├── converter/                    
│   ├── __init__.py              # Initializes the converter module
│   ├── env_json_converter.py    # Contains the core conversion logic
├── tests/                       
│   ├── __init__.py              # Optional: Shared test utilities
│   ├── test_converter.py        # Unit tests
├── .gitignore                   # Specifies files to ignore in version control
├── LICENSE                      # License file
├── README.md                    # Readme for documentation
├── requirements.txt             # Lists dependencies (if any)
├── setup.py                     # Metadata and installation details for setuptools
├── pyproject.toml               # Modern Python packaging configuration
├── setup.sh                     # Setup script for installing the package
```

## Contributing 🤝

We welcome contributions! Here's how you can get involved:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to your branch: `git push origin feature-name`.
5. Create a pull request.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Support ❤️

If you find this package useful, give it a 🌟 on GitHub and share it with your network!

