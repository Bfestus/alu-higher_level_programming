#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, element in enumerate(row):
            if index == len(row) - 1:
                print("{:d}".format(element))
            else:
                print("{:d}".format(element), end=" ")

# Example matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

