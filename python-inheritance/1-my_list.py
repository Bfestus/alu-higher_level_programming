#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
     """
    A custom list class that inherits from the built-in list class.

    Methods:
        print_sorted(): Prints the elements of the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.
        Does not modify the original list.

        Example:
            my_list = MyList()
            my_list.append(1)
            my_list.append(4)
            my_list.append(2)
            my_list.append(3)
            my_list.append(5)

            print(my_list)  # Output: [1, 4, 2, 3, 5]
            my_list.print_sorted()  # Output: [1, 2, 3, 4, 5]
            print(my_list)  # Output: [1, 4, 2, 3, 5]
        """
        sorted_list = sorted(self)
        print(sorted_list)

    def __str__(self):
        """
        Returns a string representation of the list.

        Returns:
            str: A string representing the elements of the list.

        Example:
            my_list = MyList([1, 2, 3, 4, 5])
            print(my_list)  # Output: "[1, 2, 3, 4, 5]"
        """
        return super().__str__()
