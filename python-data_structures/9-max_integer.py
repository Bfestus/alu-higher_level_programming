#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    largest_integer = my_list[0]
    for num in my_list:
        if num > largest_integer:
            largest_integer = num
    return largest_integer         
