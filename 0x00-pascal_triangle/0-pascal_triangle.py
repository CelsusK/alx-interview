#!/usr/bin/python3
"""
0. Pascal's Triangle
"""
def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row."""
    if n <= 0:
        return []

    triangle = []  # Initialize an empty list to hold the rows of the triangle

    for i in range(n):
        # Start each row with 1's
        row = [1] * (i + 1)

        # Fill in the middle values based on the sum of the two above
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)  # Add the completed row to the triangle

    return triangle

# Example usage:
rows = 5
triangle = pascal_triangle(rows)
for row in triangle:
    print(row)


