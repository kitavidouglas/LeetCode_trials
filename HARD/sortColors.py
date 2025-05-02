'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None  Do not return anything, modify nums in-place instead.
        """
        # Pointers for next positions of 0 and 2
        p0, curr = 0, 0
        p2 = len(nums) - 1
        
        # Traverse the array
        while curr <= p2:
            if nums[curr] == 0:
                # Swap current with p0, expand the 0-region
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                # Swap current with p2, shrink the 2-region
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
                # Note: do not increment curr here, need to re-examine nums[curr]
            else:
                # nums[curr] == 1, just move on
                curr += 1
