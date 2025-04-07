'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        quadruplets = []
        n = len(nums)
        
        # First loop: fix the first element.
        for i in range(n):
            # Skip duplicate elements.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Second loop: fix the second element.
            for j in range(i + 1, n):
                # Skip duplicate elements.
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # Two pointers for the remaining two elements.
                left = j + 1
                right = n - 1
                
                while left < right:
                    sum_val = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if sum_val < target:
                        left += 1
                    elif sum_val > target:
                        right -= 1
                    else:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for the third element.
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the fourth element.
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                        
        return quadruplets
