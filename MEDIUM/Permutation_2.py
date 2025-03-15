'''Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])  # Add a copy of nums to results
                return
            
            seen = set()  # Track used numbers at the current index
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue  # Skip duplicates
                
                seen.add(nums[i])  # Mark number as used at this recursion level
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1)  # Recur for the next index
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack

        nums.sort()  # Sorting helps in detecting duplicates
        result = []
        backtrack(0)
        return result
