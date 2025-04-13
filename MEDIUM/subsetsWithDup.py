class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort to handle duplicates
        result = []
        
        def backtrack(start, path):
            # Add a copy of the current path (subset) to the result
            result.append(path[:])
            # Explore further elements to add into the subset
            for i in range(start, len(nums)):
                # Skip duplicates: if the current element is the same as the previous
                # one and the previous one was not chosen in this recursive level, skip it.
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # Include nums[i] in the current subset and move forward
                path.append(nums[i])
                backtrack(i + 1, path)
                # Backtrack by removing the last element added
                path.pop()
        
        backtrack(0, [])
        return result
