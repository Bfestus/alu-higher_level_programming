#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        sorted_list = self._sort_ascending()
        for element in sorted_list:
            print(element, end=' ')
        print()
