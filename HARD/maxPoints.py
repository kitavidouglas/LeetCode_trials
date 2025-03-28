import heapq
'''
You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.

 

Example 1:


Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
Output: [5,8,1]
Explanation: The diagrams above show which cells we visit to get points for each query.
Example 2:


Input: grid = [[5,2,1],[1,1,2]], queries = [3]
Output: [0]
Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.


'''
class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right
        
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])  # Sort queries with their indices
        result = [0] * len(queries)
        visited = [[False] * n for _ in range(m)]
        
        min_heap = [(grid[0][0], 0, 0)]  # Min-heap storing (value, row, col)
        visited[0][0] = True
        points = 0  # Total points we can collect
        
        for idx, q in sorted_queries:
            while min_heap and min_heap[0][0] < q:
                val, r, c = heapq.heappop(min_heap)
                points += 1  # Earn one point for the first time visiting
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
                        visited[nr][nc] = True  # Mark as visited
            
            result[idx] = points  # Store answer for the query
        
        return result
