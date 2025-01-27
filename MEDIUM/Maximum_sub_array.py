# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize variables
        current_sum = nums[0]  # Start with the first element
        max_sum = nums[0]      # Start with the first element

        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Update current_sum: either start a new subarray or continue the current one
            current_sum = max(num, current_sum + num)
            
            # Update max_sum with the larger value between current_sum and max_sum
            max_sum = max(max_sum, current_sum)
        
        return max_sum

# Sample main function to compute the result of maxSubArray
def main():
    solution = Solution()

    # Test case 1: Array with a mix of positive and negative numbers
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result1 = solution.maxSubArray(nums1)
    print(f"Max subarray sum of {nums1} is: {result1}")

    # Test case 2: Array with all negative numbers
    nums2 = [-1, -2, -3, -4]
    result2 = solution.maxSubArray(nums2)
    print(f"Max subarray sum of {nums2} is: {result2}")

    # Test case 3: Array with all positive numbers
    nums3 = [1, 2, 3, 4]
    result3 = solution.maxSubArray(nums3)
    print(f"Max subarray sum of {nums3} is: {result3}")

# Run the main function
main()
