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

    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digit_sum_map = {}
        max_sum = -1

        # Helper function to calculate sum of digits
        def sum_of_digits(num):
            return sum(int(digit) for digit in str(num))

        for num in nums:
            digit_sum = sum_of_digits(num)
            if digit_sum in digit_sum_map:
                max_sum = max(max_sum, num + digit_sum_map[digit_sum])
                digit_sum_map[digit_sum] = max(digit_sum_map[digit_sum], num)
            else:
                digit_sum_map[digit_sum] = num

        return max_sum

# Example usage:
solution = Solution()
print(solution.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))  # Output: 4
print(solution.magnificentSets(3, [[1,2],[2,3],[3,1]]))  # Output: -1

print(solution.maximumSum([51, 71, 17, 42]))  # Output: 93 (71 + 51)
print(solution.maximumSum([42, 33, 60]))  # Output: 102 (42 + 60)
print(solution.maximumSum([10, 20, 30]))  # Output: -1 (No two numbers with the same digit sum)
