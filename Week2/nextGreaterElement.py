def nextGreaterElement(nums1, nums2):
    next_greater = {}
    stack = []

    # Find the next greater element for each element in nums2
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)

    # Initialize result array with -1
    ans = [-1] * len(nums1)

    # Find the next greater element for each element in nums1
    for i, num in enumerate(nums1):
        if num in next_greater:
            ans[i] = next_greater[num]

    return ans

# Example usage
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))  # Output: [-1, 3, -1]

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(nextGreaterElement(nums1, nums2))  # Output: [3, -1]
