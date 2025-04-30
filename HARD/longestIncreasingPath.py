'''
From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1

'''
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        # memo[i][j] will store the length of the longest increasing path starting at (i, j)
        memo = [[0] * n for _ in range(m)]
        # four possible move directions
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i, j):
            # if already computed, return it
            if memo[i][j] != 0:
                return memo[i][j]

            best = 1  # at least the cell itself
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                # move only if next cell is within bounds and strictly greater
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    length = 1 + dfs(ni, nj)
                    best = max(best, length)

            memo[i][j] = best
            return best

        ans = 0
        # compute dfs from every cell, track the maximum
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        return ans
