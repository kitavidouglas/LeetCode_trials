''' You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

'''
class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        island_sizes = {0: 0}  # Store island sizes, 0 for water
        island_id = 2  # Start labeling islands from 2
        
        def dfs(r, c, island_id):
            """ Perform DFS to calculate island size. """
            stack = [(r, c)]
            grid[r][c] = island_id
            size = 0
            
            while stack:
                x, y = stack.pop()
                size += 1
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = island_id
                        stack.append((nx, ny))
            return size
        
        # Step 1: Find all islands and store their sizes
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[island_id] = dfs(r, c, island_id)
                    island_id += 1
        
        # Step 2: Find the largest possible island
        max_island = max(island_sizes.values())  # Max existing island size
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:  # Try flipping this zero
                    seen = set()
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])  # Collect adjacent island IDs
                    
                    # Compute new possible island size
                    new_size = 1 + sum(island_sizes[i] for i in seen)
                    max_island = max(max_island, new_size)
        
        return max_island

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    grid1 = [[1, 0], 
             [0, 1]]
    print(sol.largestIsland(grid1))  # Expected output: 3

    # Test Case 2
    grid2 = [[1, 1], 
             [1, 0]]
    print(sol.largestIsland(grid2))  # Expected output: 4

    # Test Case 3
    grid3 = [[1, 1], 
             [1, 1]]
    print(sol.largestIsland(grid3))  # Expected output: 4

    # Test Case 4 (Larger Grid)
    grid4 = [[1, 0, 1], 
             [1, 0, 1], 
             [1, 1, 1]]
    print(sol.largestIsland(grid4))  # Expected output: 7
