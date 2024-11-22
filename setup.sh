#!/bin/bash

# Ensure Python 3.7+ is available
if ! python3 --version | grep -q "Python 3"; then
  echo "Python 3.7+ is required. Please install it and try again."
  exit 1
fi

# Create and activate virtual environment
python3 -m venv env
source env/bin/activate

# Install the package
pip install .

echo "Setup complete! Virtual environment activated. Use 'deactivate' to exit."
