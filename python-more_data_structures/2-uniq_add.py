#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_integers = set()
    for num in my_list:
        # Add the integer to the set
        unique_integers.add(num)
    # Calculate the sum of the unique integers
    sum_unique = sum(unique_integers)
    return sum_unique
