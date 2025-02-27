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
