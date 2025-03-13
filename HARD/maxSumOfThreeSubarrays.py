'''Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically smaller.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]

'''

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        sum_k = [0] * (n - k + 1)  # Store sum of subarrays of length k
        
        # Compute sum of each subarray of length k
        window_sum = sum(nums[:k])
        sum_k[0] = window_sum
        for i in range(1, n - k + 1):
            window_sum += nums[i + k - 1] - nums[i - 1]
            sum_k[i] = window_sum

        # Arrays to store best left and right indices
        left = [0] * (n - k + 1)
        right = [0] * (n - k + 1)

        # Compute best left index for each position
        best_left = 0
        for i in range(n - k + 1):
            if sum_k[i] > sum_k[best_left]:  # Find max sum on left side
                best_left = i
            left[i] = best_left

        # Compute best right index for each position
        best_right = n - k
        for i in range(n - k, -1, -1):
            if sum_k[i] >= sum_k[best_right]:  # Find max sum on right side
                best_right = i
            right[i] = best_right

        # Find the three non-overlapping subarrays with max sum
        max_sum = 0
        result = []
        for mid in range(k, n - 2 * k + 1):
            l, r = left[mid - k], right[mid + k]
            total = sum_k[l] + sum_k[mid] + sum_k[r]
            if total > max_sum:
                max_sum = total
                result = [l, mid, r]

        return result
