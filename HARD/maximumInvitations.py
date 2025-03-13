'''
A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.

The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.

Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.

 

Example 1:


Input: favorite = [2,2,1,2]
Output: 3
Explanation:
The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
The maximum number of employees that can be invited to the meeting is 3. 
Example 2:

Input: favorite = [1,2,0]
Output: 3
Explanation: 
Each employee is the favorite person of at least one other employee, and the only way the company can invite them is if they invite every employee.
The seating arrangement will be the same as that in the figure given in example 1:
- Employee 0 will sit between employees 2 and 1.
- Employee 1 will sit between employees 0 and 2.
- Employee 2 will sit between employees 1 and 0.
The maximum number of employees that can be invited to the meeting is 3.
Example 3:


Input: favorite = [3,0,1,4,1]
Output: 4
Explanation:
The above figure shows how the company will invite employees 0, 1, 3, and 4, and seat them at the round table.
Employee 2 cannot be invited because the two spots next to their favorite employee 1 are taken.
So the company leaves them out of the meeting.
The maximum number of employees that can be invited to the meeting is 4.

'''

class Solution(object):
    def maximumInvitations(self, favorite):
        """
        :type favorite: List[int]
        :rtype: int
        """
        from collections import defaultdict, deque
        
        n = len(favorite)
        indegree = [0] * n
        adj_list = defaultdict(list)
        
        # Build graph
        for i, f in enumerate(favorite):
            adj_list[f].append(i)
            indegree[i] += 1
        
        # Step 1: Find longest chains ending in mutual favorite pairs
        queue = deque()
        longest_chain = [1] * n  # Track longest path to a node
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            fav = favorite[node]
            longest_chain[fav] = max(longest_chain[fav], longest_chain[node] + 1)
            indegree[fav] -= 1
            if indegree[fav] == 0:
                queue.append(fav)

        # Step 2: Detect cycles and find the longest one
        visited = [False] * n
        max_cycle_size = 0
        two_node_cycles_sum = 0
        
        for i in range(n):
            if visited[i]:
                continue

            # Detect cycles using slow/fast pointers
            slow, fast = i, favorite[i]
            while not visited[fast]:
                visited[fast] = True
                fast = favorite[fast]

            # Count cycle size
            cycle_size = 1
            node = favorite[fast]
            while node != fast:
                cycle_size += 1
                node = favorite[node]

            if cycle_size == 2:
                # If it's a two-node cycle, sum up its longest chains
                two_node_cycles_sum += longest_chain[fast] + longest_chain[favorite[fast]]
            else:
                max_cycle_size = max(max_cycle_size, cycle_size)

        return max(max_cycle_size, two_node_cycles_sum)
