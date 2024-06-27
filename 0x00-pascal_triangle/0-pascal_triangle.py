#!/usr/bin/python3
"""Construct Pascal's triangle for any number n"""

def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's triangle where each numbers is displayed in rows showing a computation of low below a computation of low above with 1 at the edge of the rows

    Args:
        n: number of rows to display in the triangle
    """
    # initializing the triangle
    triangle = []
    if n <= 0:
        """return empty array if n is less than 0"""
        return triangle
    for i in range(n):
        """create an array of numbers representing the number of n and the arrays of number length will be equal to the loop of the n"""
        row = []
        for j in range(i+1):
            """create and array from the array of numbers in rows"""
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # add completed row in the triangle
        triangle.append(row)
    return triangle
