#!/usr/bin/python3


def pascal_triangle(n):
    """
    Pascal's triangle
    Args:
      n (int): The number of rows of the triangle
    Returns:
      List of lists of integers representing the Pascal’s triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1] + [prev_row[j - 1] + prev_row[j] for j in range(1, i)] + [1]
        triangle.append(new_row)

    return triangle
