''' 
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        prefix = strs[0]  # Start with the first string as the prefix
        
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:  # Check if the prefix is a prefix of strs[i]
                prefix = prefix[:-1]  # Reduce the prefix
                if not prefix:
                    return ""
        
        return prefix
