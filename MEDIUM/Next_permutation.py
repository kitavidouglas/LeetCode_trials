'''A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, 
if all the permutations of the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted container. 
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).'''



class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the first element that is smaller than its next element.
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:  # If a valid 'i' is found (i.e., not the last permutation)
            # Step 2: Find the smallest number larger than nums[i] from the right side
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the portion of the list after index i to get the next smallest lexicographical order
        nums[i + 1:] = nums[i + 1:][::-1]

# Sample main function to compute sample values
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Simple permutation
    nums1 = [1, 2, 3]
    print(f"Original list: {nums1}")
    solution.nextPermutation(nums1)
    print(f"Next permutation: {nums1}\n")

    # Test case 2: Next permutation for a list with repeated numbers
    nums2 = [1, 3, 2]
    print(f"Original list: {nums2}")
    solution.nextPermutation(nums2)
    print(f"Next permutation: {nums2}\n")

    # Test case 3: The list is already in the highest permutation
    nums3 = [3, 2, 1]
    print(f"Original list: {nums3}")
    solution.nextPermutation(nums3)
    print(f"Next permutation: {nums3}\n")

    # Test case 4: The list is already in the lowest permutation
    nums4 = [1, 1, 5]
    print(f"Original list: {nums4}")
    solution.nextPermutation(nums4)
    print(f"Next permutation: {nums4}\n")

    # Test case 5: Single element list
    nums5 = [1]
    print(f"Original list: {nums5}")
    solution.nextPermutation(nums5)
    print(f"Next permutation: {nums5}\n")
