#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for key in a_dictionary:
        #a values
        values = a_dictionary[key]
        print(values * 2)
    return a_dictionary    
