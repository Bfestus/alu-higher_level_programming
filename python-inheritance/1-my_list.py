#!/usr/bin/python3
"""define the subclass my_list from list
"""


class my_list(list):
  """initialize the list"""
  def __init__(self):
    super().__init__()
    
  def print_sorted(self):
    """ printing the list sorted from ascending order,
    we just create variable called sorted to sort our list
    by using sorted() key word 
    """
    sorted = sorted(list)
    print(int(sorted))
