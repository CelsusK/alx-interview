#!/usr/bin/python3
def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row."""
    if n <= 0:
        return []  # Return an empty list for n <= 0

    triangle = []  # Initialize an empty list to hold the rows of the triangle

    for i in range(n):
        # Start each row with 1's
        row = [1] * (i + 1)

        # Fill in the middle values based on the sum of the two above
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)  # Add the completed row to the triangle

    return triangle

# Example usage to test the function
if __name__ == "__main__":
    # You can test the function using the provided test script
    triangle = pascal_triangle(5)
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
