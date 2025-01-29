'''In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

'''

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = {}  # Dictionary to store the parent of each node
        
        def find(x):
            """Finds the root of the node using path compression."""
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            """Unites two sets and returns False if they are already connected."""
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False  # Cycle detected
            parent[rootY] = rootX  # Union the sets
            return True
        
        # Initialize the parent dictionary
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            if not union(u, v):  # If union returns False, this edge is redundant
                return [u, v]

# Example usage:
solution = Solution()
print(solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # Output: [2, 3]
print(solution.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # Output: [1, 4]
