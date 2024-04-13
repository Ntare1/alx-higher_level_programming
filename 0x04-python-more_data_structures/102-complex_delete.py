#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for x in a_dictionary:
        if a_dictionary[x] == value:
            keys.append(x)
    for key in keys:
        del a_dictionary[x]
    return(a_dictionary)
