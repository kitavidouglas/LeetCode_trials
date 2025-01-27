#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.



class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Step 1: Transpose the matrix (swap elements across the diagonal)
        for i in range(n):
            for j in range(i + 1, n):  # Swap only upper triangle to avoid double swap
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()  # Reverse the elements of the row in-place

    # Helper method to print the matrix
    def printMatrix(self, matrix):
        for row in matrix:
            print(" ".join(map(str, row)))

# Sample main to test the rotation
if __name__ == "__main__":
    solution = Solution()
    
    # Sample 3x3 matrix
    matrix = [
        [7, 9, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Original Matrix:")
    solution.printMatrix(matrix)
    
    # Rotate the matrix by 90 degrees
    solution.rotate(matrix)
    
    print("\nMatrix After Rotation:")
    solution.printMatrix(matrix)
