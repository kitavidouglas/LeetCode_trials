'''
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

 

Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0
 

Constraints:

0 <= left <= right <= 231 - 1


'''

class Solution(object):
    def c(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # count how many trailing bits we've shifted off
        shift = 0
        
        # while the numbers differ, shift both right
        # this effectively finds the common high-order bits
        while left < right:
            left  >>= 1
            right >>= 1
            shift += 1
        
        # shift the common prefix bits back to their original positions
        return left << shift
