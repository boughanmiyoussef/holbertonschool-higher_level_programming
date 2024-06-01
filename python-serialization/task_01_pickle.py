#!/usr/bin/python3
"""
This module defines a custom class for serialization and deserialization
using the pickle module.
"""

import pickle

class CustomObject:
    """
    A custom class that represents a person with name, age, and student status.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a new instance of CustomObject.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): The student status of the person.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints out the object's attributes in a formatted string.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to the specified file.

        Args:
            filename (str): The name of the file to save the serialized object.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an instance from the specified file.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject: The deserialized instance of CustomObject.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Error deserializing object: {e}")
            return None

if __name__ == "__main__":
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    obj.serialize("object.pkl")

    new_obj = CustomObject.deserialize("object.pkl")
    print("\nDeserialized Object:")
    if new_obj:
        new_obj.display()
    else:
        print("Failed to deserialize object.")
