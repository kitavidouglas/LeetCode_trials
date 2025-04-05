'''
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1

'''

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i] will store the number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        
        # Build the solution for every number of nodes from 2 to n
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
                
        return dp[n]
