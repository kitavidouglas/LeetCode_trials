'''Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10

'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start):
            # If we have a complete permutation, add it to the result
            if start == len(nums):
                result.append(nums[:])  # Make a copy of nums
                return
            
            for i in range(start, len(nums)):
                # Swap to create a new permutation
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)  # Recur for next index
                # Swap back to restore the original order (backtracking)
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0)
        return result
