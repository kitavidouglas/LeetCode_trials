class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def canSplit(nums, k, max_sum):
            """
            Helper function to check if it's possible to split the array
            into `k` subarrays with the largest sum <= `max_sum`.
            """
            current_sum = 0
            subarrays_count = 1  # Start with 1 subarray
            
            for num in nums:
                if current_sum + num > max_sum:
                    # If adding this number exceeds max_sum, start a new subarray
                    subarrays_count += 1
                    current_sum = num  # Start a new subarray with this number
                    if subarrays_count > k:  # If we exceed `k` subarrays, return False
                        return False
                else:
                    current_sum += num  # Add number to the current subarray
            
            return True
        
        # Binary search for the smallest possible largest sum
        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            if canSplit(nums, k, mid):
                right = mid  # Try a smaller largest sum
            else:
                left = mid + 1  # Increase the smallest largest sum
        
        return left

# Sample main function to compute the result of splitArray
def main():
    solution = Solution()

    # Test case 1: Array with a mix of positive numbers and multiple splits
    nums1 = [7, 2, 5, 10, 8]
    k1 = 2
    result1 = solution.splitArray(nums1, k1)
    print(f"Minimum largest sum of {nums1} split into {k1} subarrays is: {result1}")

    # Test case 2: Array with only one number, no split needed
    nums2 = [10]
    k2 = 1
    result2 = solution.splitArray(nums2, k2)
    print(f"Minimum largest sum of {nums2} split into {k2} subarrays is: {result2}")

    # Test case 3: Array with large numbers and multiple splits
    nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k3 = 3
    result3 = solution.splitArray(nums3, k3)
    print(f"Minimum largest sum of {nums3} split into {k3} subarrays is: {result3}")

# Run the main function
main()

import heapq

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)  # Convert nums into a min-heap
        operations = 0

        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)  # Smallest element
            y = heapq.heappop(nums)  # Second smallest element
            new_value = x * 2 + y  # Apply the operation
            heapq.heappush(nums, new_value)  # Insert the new value into the heap
            operations += 1

        return operations if nums[0] >= k else -1  # If all elements are >= k, return operations count, else -1

# Example usage:
solution = Solution()
print(solution.minOperations([2, 11, 10, 1, 3], 10))  # Output: 2
print(solution.minOperations([1, 1, 2, 4, 9], 20))    # Output: 4


import heapq

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)  # Convert nums into a min-heap
        operations = 0

        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)  # Smallest element
            y = heapq.heappop(nums)  # Second smallest element
            new_value = x * 2 + y  # Apply the operation
            heapq.heappush(nums, new_value)  # Insert the new value into the heap
            operations += 1

        return operations if nums[0] >= k else -1  # If all elements are >= k, return operations count, else -1

# Example usage:
solution = Solution()
print(solution.minOperations([2, 11, 10, 1, 3], 10))  # Output: 2
print(solution.minOperations([1, 1, 2, 4, 9], 20))    # Output: 4

import heapq

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)  # Convert nums into a min-heap
        operations = 0

        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)  # Smallest element
            y = heapq.heappop(nums)  # Second smallest element
            new_value = x * 2 + y  # Apply the operation
            heapq.heappush(nums, new_value)  # Insert the new value into the heap
            operations += 1

        return operations if nums[0] >= k else -1  # If all elements are >= k, return operations count, else -1

# Example usage:
solution = Solution()
print(solution.minOperations([2, 11, 10, 1, 3], 10))  # Output: 2
print(solution.minOperations([1, 1, 2, 4, 9], 20))    # Output: 4

import heapq

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)  # Convert nums into a min-heap
        operations = 0

        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)  # Smallest element
            y = heapq.heappop(nums)  # Second smallest element
            new_value = x * 2 + y  # Apply the operation
            heapq.heappush(nums, new_value)  # Insert the new value into the heap
            operations += 1

        return operations if nums[0] >= k else -1  # If all elements are >= k, return operations count, else -1

# Example usage:
solution = Solution()
print(solution.minOperations([2, 11, 10, 1, 3], 10))  # Output: 2
print(solution.minOperations([1, 1, 2, 4, 9], 20))    # Output: 4
