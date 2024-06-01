#!/usr/bin/python3
"""
This module defines functions for serializing a Python dictionary to XML
and deserializing XML to a Python dictionary.
"""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the XML file to save the serialized data.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserializes an XML file to a Python dictionary.

    Args:
        filename (str): The name of the XML file to read the data from.

    Returns:
        dict: The deserialized Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {child.tag: child.text for child in root}

    return dictionary

if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)
