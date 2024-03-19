def findMaxConsecutiveOnes(nums):
    max_consecutive = 0
    current_consecutive = 0

    for num in nums:
        if num == 1:
            current_consecutive += 1
            max_consecutive = max(max_consecutive, current_consecutive)
        else:
            current_consecutive = 0

    return max_consecutive

# Example usage
nums1 = [1, 1, 0, 1, 1, 1]
nums2 = [1, 0, 1, 1, 0, 1]

print(findMaxConsecutiveOnes(nums1))  # Output: 3
print(findMaxConsecutiveOnes(nums2))  # Output: 2
