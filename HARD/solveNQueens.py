'''The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]

'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
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
                result.append(["." * col + "Q" + "." * (n - col - 1) for col in board])
                return

            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(row + 1, board)
                    board[row] = -1  # Backtrack

        result = []
        solve(0, [-1] * n)
        return result
