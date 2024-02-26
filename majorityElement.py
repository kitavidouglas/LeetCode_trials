def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

# Test the function
nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print("Majority element:", majorityElement(nums))
