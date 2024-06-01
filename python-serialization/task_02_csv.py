#!/usr/bin/python3
"""
This module defines a function to convert a CSV file to a JSON file.
"""

import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file.

    Args:
        csv_filename (str): The name of the CSV file to be converted.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = [row for row in csv_reader]
        
        with open('data.json', mode='w') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"File {csv_filename} not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    csv_file = "data.csv"
    if convert_csv_to_json(csv_file):
        print(f"Data from {csv_file} has been converted to data.json")
    else:
        print("Conversion failed.")
