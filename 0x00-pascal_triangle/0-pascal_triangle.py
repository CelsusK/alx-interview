#!/usr/bin/python3
def pascal_triangle(n):
    triangle = []

    for i in range(n):
        # Start with a row of 1's (length = i+1)
        row = [1] * (i + 1)

        # Fill in the middle values based on the sum of the two above
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        # Add the completed row to the triangle
        triangle.append(row)

    return triangle

# Example usage:
rows = 5
triangle = pascal_triangle(rows)
for row in triangle:
    print(row)

