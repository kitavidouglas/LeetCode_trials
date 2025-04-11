class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Phase 1: place each number x in position x-1, whenever possible
        for i in range(n):
            # while nums[i] is in [1..n] and not already in the right spot,
            # swap it to its correct position nums[i]-1
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # swap nums[i] with nums[nums[i]-1]
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                # after swap, nums[i] is the new value to check in the next loop
        
        # Phase 2: the first index i for which nums[i] != i+1 is our answer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # if all 1..n are in place, then the answer is n+1
        return n + 1
