"""
Problem 1: Transpose Matrix
Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.

############### UMPIRE Method ###############

1. Understand
Input: a 2D integer list matrix
Output: a new 2D list that is the transpose of matrix
Rows become columns and columns become rows.
Edge case: empty matrix -> empty list

2. Match
This is a matrix traversal problem.
We need to visit each column, then collect values from each row.

3. Plan
If matrix is empty, return an empty list.
Loop through each column index.
For each column, create a new row.
Loop through each row and add matrix[row][column] to the new row.
Add the new row to the output.
Return output.

4. Implement
Use nested for loops.
The outer loop goes through columns.
The inner loop goes through rows.

5. Review
For [[1, 2, 3], [4, 5, 6]]:
Column 0 -> [1, 4]
Column 1 -> [2, 5]
Column 2 -> [3, 6]
Return [[1, 4], [2, 5], [3, 6]]

6. Evaluate
Time complexity: O(m * n), where m is the number of rows and n is the number of columns.
Space complexity: O(m * n), because we create a new transposed matrix.

"""

def transpose(matrix):
    if not matrix:
        return []

    output = []
    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        output.append(new_row)

    return output

# Example Usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))


# Example Output:
# [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# ]
# [
#     [1, 4],
#     [2, 5],
#     [3, 6]
# ]