from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i  # Return the index if target is found or the position to insert
        return len(nums)  # If the target is greater than all elements, insert at the end

# Test the function
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    index = solution.searchInsert(nums, target)
    print("Index of target or the position to insert it:", index)
