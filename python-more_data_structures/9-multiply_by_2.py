#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    abc = a_dictionary.copy()
    for i, j in abc.items():
        abc[i] = j * 2
    return (abc)