'''You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
'''
class Solution(object):
    def findTargetSumWays(self, nums, target):
        total_sum = sum(nums)
        
        # If the sum of nums + target is odd, it's impossible to divide it into two equal subsets
        if (total_sum + target) % 2 != 0:
            return 0
        
        # Find the subset sum we need to achieve
        subset_sum = (total_sum + target) // 2
        
        # Initialize DP array where dp[i] will store the number of ways to get sum i
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # There's one way to make sum 0 (by selecting no elements)
        
        # Update dp array based on the numbers in nums
        for num in nums:
            for i in range(subset_sum, num - 1, -1):
                dp[i] += dp[i - num]
        
        return dp[subset_sum]
