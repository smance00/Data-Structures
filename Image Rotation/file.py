matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Function to rotate the matrix by 90 degrees clockwise
def rotate_matrix(matrix):
    n = len(matrix)

    # Initialize a new matrix of the same size
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Rotate the matrix by 90 degrees
    # by assigning the values with the corresponding rotated indices
    for i in range(n):
        for j in range(n):
            new_matrix[j][n-1-i] = matrix[i][j]

    # Update the original matrix with the rotated values
    for i in range(n):
        for j in range(n):
            matrix[i][j] = new_matrix[i][j]

# Print the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Call the function to rotate the matrix
rotate_matrix(matrix)

# Print the rotated matrix
print("\nMatrix after rotation:")
for row in matrix:
    print(row)

    # Function to rotate the matrix by 90 degrees clockwise without allocating new 2D array
def rotate_matrix1(matrix):
    n = len(matrix)

    # Exchange elements in top row to bottom row
    for i in range(n // 2):
        matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]

    # Swap the symmetry elements
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix

# Print the original matrix
print("Original Matrix_1:")
for row in matrix_1:
    print(row)

# Call the function to rotate the matrix
rotated_matrix = rotate_matrix1(matrix_1)

# Print the rotated matrix
print("\nMatrix_1 after rotation:")
for row in rotated_matrix:
    print(row)