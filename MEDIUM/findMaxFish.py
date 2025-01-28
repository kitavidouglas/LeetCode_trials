'''
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

'''

class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Directions for moving up, down, left, and right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Helper function to perform DFS and collect fish
        def dfs(r, c):
            # Initialize the fish count for this component
            fish_count = grid[r][c]
            grid[r][c] = 0  # Mark the cell as visited by setting it to 0
            
            # Explore all four adjacent directions (up, down, left, right)
            for dx, dy in directions:
                nx, ny = r + dx, c + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                    fish_count += dfs(nx, ny)  # Recursively collect fish from adjacent cells
            return fish_count
        
        max_fish = 0  # To track the maximum fish caught
        
        # Iterate through all cells in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:  # If the cell contains fish
                    max_fish = max(max_fish, dfs(i, j))  # Get the maximum fish count from DFS
        
        return max_fish
