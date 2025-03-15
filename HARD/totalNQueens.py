'''The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1

'''

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_safe(board, row, col):
            # Check column
            for i in range(row):
                if board[i] == col:
                    return False
            # Check diagonals
            for i, j in enumerate(range(row - 1, -1, -1)):
                if board[j] == col - (row - j) or board[j] == col + (row - j):
                    return False
            return True

        def solve(row, board):
            if row == n:
                self.count += 1
                return

            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(row + 1, board)
                    board[row] = -1  # Backtrack

        self.count = 0
        solve(0, [-1] * n)
        return self.count
