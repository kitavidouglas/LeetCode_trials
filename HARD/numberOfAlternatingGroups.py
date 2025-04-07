'''
There are some red and blue tiles arranged circularly. You are given an array of integers colors and a 2D integers array queries.

The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is a contiguous subset of tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its adjacent tiles in the group).

You have to process queries of two types:

queries[i] = [1, sizei], determine the count of alternating groups with size sizei.
queries[i] = [2, indexi, colori], change colors[indexi] to colori.
Return an array answer containing the results of the queries of the first type in order.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

Example 1:

Input: colors = [0,1,1,0,1], queries = [[2,1,0],[1,4]]

Output: [2]

Explanation:



First query:

Change colors[1] to 0.



Second query:

Count of the alternating groups with size 4:



Example 2:

Input: colors = [0,0,1,0,1,1], queries = [[1,3],[2,3,0],[1,5]]

Output: [2,0]

Explanation:



First query:

Count of the alternating groups with size 3:



Second query: colors will not change.

Third query: There is no alternating group with size 5
'''

class FenwTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def build(self, arr):
        for i in range(self.n):
            self.update(i, arr[i])
    
    def update(self, i, delta):
        # i is 0-indexed; tree index is i+1.
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i
            
    def query(self, i):
        # sum from index 0 to i inclusive.
        s = 0
        i += 1
        while i:
            s += self.tree[i]
            i -= i & -i
        return s
    
    def range_sum(self, l, r):
        if l > r:
            return 0
        return self.query(r) - (self.query(l-1) if l > 0 else 0)


class Solution(object):
    def numberOfAlternatingGroups(self, colors, queries):
        """
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(colors)
        if n == 0:
            return []
        
        # Build diff array: diff[i] = 1 if colors[i] != colors[(i+1) mod n], else 0.
        diff = [0] * n
        for i in range(n):
            next_i = (i + 1) % n
            diff[i] = 1 if colors[i] != colors[next_i] else 0
        
        # Build Fenwick tree over diff.
        fenw = FenwTree(n)
        fenw.build(diff)
        
        ans = []
        
        for q in queries:
            if q[0] == 1:
                # Query type 1: count the number of alternating groups of given size.
                size = q[1]
                count = 0
                if size == 1:
                    # Every tile is a group of size 1.
                    count = n
                else:
                    length = size - 1  # number of transitions that must be 1.
                    for start in range(n):
                        # The segment covers indices [start, start+length-1] in the diff array, modulo n.
                        end = (start + length - 1) % n
                        if start <= end:
                            total = fenw.range_sum(start, end)
                        else:
                            # Wrap-around: sum from start to n-1 and from 0 to end.
                            total = fenw.range_sum(start, n - 1) + fenw.range_sum(0, end)
                        if total == length:
                            count += 1
                ans.append(count)
            elif q[0] == 2:
                # Query type 2: update a tile's color.
                index, new_color = q[1], q[2]
                if colors[index] == new_color:
                    continue  # no change
                old_color = colors[index]
                colors[index] = new_color
                # The update affects diff for tile index-1 and tile index.
                # Update diff for predecessor index (prev index, circularly)
                pred = (index - 1) % n
                old_val = diff[pred]
                new_val = 1 if colors[pred] != colors[index] else 0
                diff[pred] = new_val
                fenw.update(pred, new_val - old_val)
                
                # Update diff for current index.
                succ = (index + 1) % n
                old_val = diff[index]
                new_val = 1 if colors[index] != colors[succ] else 0
                diff[index] = new_val
                fenw.update(index, new_val - old_val)
                
        return ans


# Example usage:
if __name__ == "__main__":
    # Example 1:
    colors1 = [0, 1, 1, 0, 1]
    queries1 = [[2, 1, 0], [1, 4]]
    sol = Solution()
    print("Example 1 Output:", sol.numberOfAlternatingGroups(colors1, queries1))
    # Expected Output: [2]
    
    # Example 2:
    colors2 = [0, 0, 1, 0, 1, 1]
    queries2 = [[1, 3], [2, 3, 0], [1, 5]]
    print("Example 2 Output:", sol.numberOfAlternatingGroups(colors2, queries2))
    # Expected Output: [2, 0]
