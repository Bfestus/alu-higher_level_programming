#!/usr/bin/python3
def number_keys(a_dictionary):
    key_list = []
    for key in a_dictionary:
        key_list.append(key)
    key_sum = len(key_list)
    print("{:d}".format(key_sum))
