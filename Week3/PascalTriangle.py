def generate(numRows):
    # Initialize the result list with the first row
    triangle = [[1]]
    
    # Iterate to generate the subsequent rows
    for i in range(1, numRows):
        # Initialize the current row with the first element
        row = [1]
        # Calculate the elements of the current row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # Add the last element of the row
        row.append(1)
        # Append the current row to the result
        triangle.append(row)
    
    return triangle

# Example usage
numRows = 5
print(generate(numRows))  # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
