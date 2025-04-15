''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()

''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()


''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()

''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.  '''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []  # This will hold the triplets

        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move right pointer to the left

        return result

# Sample main function to compute the result of threeSum
def main():
    solution = Solution()

    # Test case 1: Array with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"ThreeSum of {nums1} is: {result1}")

    # Test case 2: Array with no triplet
    nums2 = [1, 2, -2, -1]
    result2 = solution.threeSum(nums2)
    print(f"ThreeSum of {nums2} is: {result2}")

    # Test case 3: Array with one triplet
    nums3 = [-1, 0, 1]
    result3 = solution.threeSum(nums3)
    print(f"ThreeSum of {nums3} is: {result3}")

# Run the main function
main()
