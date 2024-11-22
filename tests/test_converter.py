import os
import json
import tempfile
from converter.env_json_converter import env_to_json, json_to_env


def create_temp_file(contents, suffix):
    """
    Helper function to create a temporary file with the given contents and suffix.
    """
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    with open(temp_file.name, "w") as file:
        file.write(contents)
    return temp_file.name


def read_file(file_path):
    """
    Helper function to read the contents of a file.
    """
    with open(file_path, "r") as file:
        return file.read()


def test_env_to_json():
    """
    Test converting a .env file to JSON.
    """
    # Sample .env contents
    env_contents = """KEY1=VALUE1
                    KEY2=VALUE2
                    KEY_WITH_SPACES = Value With Spaces
                    # Commented Line
                    KEY_WITH_EQUALS=Value=With=Equals
                    """

    # Create a temporary .env file
    env_file = create_temp_file(env_contents, ".env")
    json_file = tempfile.NamedTemporaryFile(delete=False, suffix=".json").name

    try:
        # Convert .env to JSON
        env_to_json(env_file, json_file)

        # Verify JSON contents
        with open(json_file, "r") as f:
            json_data = json.load(f)

        assert json_data["KEY1"] == "VALUE1"
        assert json_data["KEY2"] == "VALUE2"
        assert json_data["KEY_WITH_SPACES"] == "Value With Spaces"
        assert json_data["KEY_WITH_EQUALS"] == "Value=With=Equals"

    finally:
        # Clean up temporary files
        os.remove(env_file)
        os.remove(json_file)


def test_json_to_env():
    """
    Test converting a JSON file to .env.
    """
    # Sample JSON contents
    json_contents = {
        "KEY1": "VALUE1",
        "KEY2": "VALUE2",
        "KEY_WITH_SPACES": "Value With Spaces",
        "KEY_WITH_EQUALS": "Value=With=Equals"
    }

    # Create a temporary JSON file
    json_file = create_temp_file(json.dumps(json_contents), ".json")
    env_file = tempfile.NamedTemporaryFile(delete=False, suffix=".env").name

    try:
        # Convert JSON to .env
        json_to_env(json_file, env_file)

        # Verify .env contents
        with open(env_file, "r") as f:
            env_data = f.read()

        assert "KEY1=VALUE1" in env_data
        assert "KEY2=VALUE2" in env_data
        assert "KEY_WITH_SPACES=Value With Spaces" in env_data
        assert "KEY_WITH_EQUALS=Value=With=Equals" in env_data

    finally:
        # Clean up temporary files
        os.remove(json_file)
        os.remove(env_file)


def test_empty_env_to_json():
    """
    Test converting an empty .env file to JSON.
    """
    # Create an empty .env file
    env_file = create_temp_file("", ".env")
    json_file = tempfile.NamedTemporaryFile(delete=False, suffix=".json").name

    try:
        # Convert .env to JSON
        env_to_json(env_file, json_file)

        # Verify JSON contents
        with open(json_file, "r") as f:
            json_data = json.load(f)

        assert json_data == {}

    finally:
        # Clean up temporary files
        os.remove(env_file)
        os.remove(json_file)


def test_empty_json_to_env():
    """
    Test converting an empty JSON file to .env.
    """
    # Create an empty JSON file
    json_file = create_temp_file("{}", ".json")
    env_file = tempfile.NamedTemporaryFile(delete=False, suffix=".env").name

    try:
        # Convert JSON to .env
        json_to_env(json_file, env_file)

        # Verify .env contents
        env_data = read_file(env_file)
        assert env_data == ""

    finally:
        # Clean up temporary files
        os.remove(json_file)
        os.remove(env_file)
