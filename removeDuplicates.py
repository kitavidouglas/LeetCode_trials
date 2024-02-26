def removeDuplicates(nums):
    if len(nums) == 0:
        return 0

    unique_elements = 1  # At least the first element is unique

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[unique_elements] = nums[i]
            unique_elements += 1

    return unique_elements

# Test the function
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = removeDuplicates(nums)
print("Number of unique elements:", k)
print("Updated array:", nums[:k])
