#!/usr/bin/python3
"""
This module provides functions to serialize a Python dictionary to a JSON file
and deserialize a JSON file to recreate the Python dictionary.
"""

import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The filename of the output JSON file. If the file
                        already exists, it will be replaced.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load and deserialize a Python dictionary from a JSON file.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    serialize_and_save_to_file(data_to_serialize, 'data.json')

    print("Data serialized and saved to 'data.json'.")

    deserialized_data = load_and_deserialize('data.json')

    print("Deserialized Data:")
    print(deserialized_data)
