#Write a program to solve a Sudoku puzzle by filling the empty cells.

#A sudoku solution must satisfy all of the following rules:

#Each of the digits 1-9 must occur exactly once in each row.
#Each of the digits 1-9 must occur exactly once in each column.
#Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
#The '.' character indicates empty cells.

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def is_valid(board, row, col, num):
            # Check if the number already exists in the row
            for i in range(9):
                if board[row][i] == num:
                    return False
            # Check if the number already exists in the column
            for i in range(9):
                if board[i][col] == num:
                    return False
            # Check if the number already exists in the 3x3 sub-grid
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True
        
        def solve(board):
            # Find the next empty cell
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        # Try numbers 1-9
                        for num in '123456789':
                            if is_valid(board, row, col, num):
                                board[row][col] = num
                                if solve(board):
                                    return True
                                # If it doesn't lead to a solution, reset the cell
                                board[row][col] = '.'
                        return False
            return True
        
        # Start solving the Sudoku
        solve(board)

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    
    solution.solveSudoku(board)
    
    # Print the solved board
    for row in board:
        print(row)


