from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0  # Initialize count for elements not equal to val
        
        # Iterate through the array
        for num in nums:
            # If the current element is not equal to val
            if num != val:
                # Keep the element and update the count
                nums[count] = num
                count += 1
        
        # Return the count of elements not equal to val
        return count

# Test the function
if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    k = solution.removeElement(nums, val)
    print("Number of elements in nums which are not equal to val:", k)
    print("Modified nums array:", nums[:k])
