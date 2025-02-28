#You are given a string s. You can convert s to a 
   #palindrome by adding characters in front of it.

#Return the shortest palindrome you can find by performing this transformation.

#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

#The overall run time complexity should be O(log (m+n)). /////////

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1  # +1 for odd-length case
            
            # Handle edge cases where partition is at the boundaries
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Even total length
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                # Odd total length
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1

        raise ValueError("Input arrays are not sorted properly")

# Sample main function to compute the median
def main():
    solution = Solution()

    # Test case 1: Arrays with odd and even lengths
    nums1 = [1, 3]
    nums2 = [2]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Median of {nums1} and {nums2} is: {result}")

    # Test case 2: Arrays with equal lengths
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Median of {nums1} and {nums2} is: {result}")

    # Test case 3: Arrays with repeated elements
    nums1 = [0, 0]
    nums2 = [0, 0]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Median of {nums1} and {nums2} is: {result}")

# Run the main function
main()



''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1


''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1


''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

#You are given a string s. You can convert s to a 
   #palindrome by adding characters in front of it.

#Return the shortest palindrome you can find by performing this transformation.

#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

#The overall run time complexity should be O(log (m+n)). /////////

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1  # +1 for odd-length case
            
            # Handle edge cases where partition is at the boundaries
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Even total length
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                # Odd total length
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1

        raise ValueError("Input arrays are not sorted properly")

# Sample main function to compute the median
def main():
    solution = Solution()

    # Test case 1: Arrays with odd and even lengths
    nums1 = [1, 3]
    nums2 = [2]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Median of {nums1} and {nums2} is: {result}")

    # Test case 2: Arrays with equal lengths
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Median of {nums1} and {nums2} is: {result}")

    # Test case 3: Arrays with repeated elements
    nums1 = [0, 0]
    nums2 = [0, 0]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Median of {nums1} and {nums2} is: {result}")

# Run the main function
main()



''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1


''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1


''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1


#You are given a string s. You can convert s to a 
   #palindrome by adding characters in front of it.

#Return the shortest palindrome you can find by performing this transformation.

#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

#The overall run time complexity should be O(log (m+n)). /////////

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1  # +1 for odd-length case
            
            # Handle edge cases where partition is at the boundaries
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Even total length
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                # Odd total length
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1

        raise ValueError("Input arrays are not sorted properly")

# Sample main function to compute the median
def main():
    solution = Solution()

    # Test case 1: Arrays with odd and even lengths
    nums1 = [1, 3]
    nums2 = [2]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Median of {nums1} and {nums2} is: {result}")

    # Test case 2: Arrays with equal lengths
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Median of {nums1} and {nums2} is: {result}")

    # Test case 3: Arrays with repeated elements
    nums1 = [0, 0]
    nums2 = [0, 0]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Median of {nums1} and {nums2} is: {result}")

# Run the main function
main()



''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1


''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1


''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

#You are given a string s. You can convert s to a 
   #palindrome by adding characters in front of it.

#Return the shortest palindrome you can find by performing this transformation.

#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

#The overall run time complexity should be O(log (m+n)). /////////

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1  # +1 for odd-length case
            
            # Handle edge cases where partition is at the boundaries
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Even total length
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                # Odd total length
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1

        raise ValueError("Input arrays are not sorted properly")

# Sample main function to compute the median
def main():
    solution = Solution()

    # Test case 1: Arrays with odd and even lengths
    nums1 = [1, 3]
    nums2 = [2]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Median of {nums1} and {nums2} is: {result}")

    # Test case 2: Arrays with equal lengths
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Median of {nums1} and {nums2} is: {result}")

    # Test case 3: Arrays with repeated elements
    nums1 = [0, 0]
    nums2 = [0, 0]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Median of {nums1} and {nums2} is: {result}")

# Run the main function
main()



''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1


''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1


''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
''' You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

'''

from collections import deque, defaultdict

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Helper function to check if the graph is bipartite and return max depth
        def bfs(start):
            queue = deque([(start, 1)])  # (node, depth)
            depth_map[start] = 1
            max_depth = 1

            while queue:
                node, depth = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in depth_map:
                        depth_map[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        queue.append((neighbor, depth + 1))
                    elif abs(depth_map[neighbor] - depth) != 1:
                        return -1  # The graph is not bipartite (odd cycle found)
            
            return max_depth

        # Step 3: Find connected components and check bipartiteness
        visited = set()
        max_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = set()
                stack = [node]
                
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.add(current)
                        stack.extend(graph[current])
                
                # Find the max depth in this component
                best_depth = -1
                for start in component:
                    depth_map = {}
                    depth = bfs(start)
                    if depth == -1:
                        return -1  # The graph is not bipartite
                    best_depth = max(best_depth, depth)
                
                max_groups += best_depth
        
        return max_groups

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1
