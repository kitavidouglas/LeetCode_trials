'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        
        self.rows = len(board)
        self.cols = len(board[0])
        self.word = word
        self.board = board
        
        # visited flags
        visited = [[False]*self.cols for _ in range(self.rows)]
        
        # Try starting the DFS from every cell
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == word[0]:
                    if self._dfs(i, j, 0, visited):
                        return True
        return False
    
    def _dfs(self, i, j, idx, visited):
        # If we've matched all characters
        if idx == len(self.word):
            return True
        
        # Boundary checks and character match / visited check
        if (i < 0 or i >= self.rows or
            j < 0 or j >= self.cols or
            visited[i][j] or
            self.board[i][j] != self.word[idx]):
            return False
        
        # Mark this cell as visited
        visited[i][j] = True
        
        # Explore all 4 directions
        found = (
            self._dfs(i+1, j,   idx+1, visited) or
            self._dfs(i-1, j,   idx+1, visited) or
            self._dfs(i,   j+1, idx+1, visited) or
            self._dfs(i,   j-1, idx+1, visited)
        )
        
        # Unmark before backtracking
        visited[i][j] = False
        return found
