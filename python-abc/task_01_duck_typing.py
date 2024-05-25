#!/usr/bin/python3

"""Tests for Circle class with negative radius"""

import unittest
from task_01_duck_typing import Circle

def test_circle_negative():
    """Test Circle class with negative radius"""
    with unittest.TestCase.assertRaises(unittest.TestCase, ValueError):
        circle_negative = Circle(radius=-5)

if __name__ == "__main__":
    test_circle_negative()
