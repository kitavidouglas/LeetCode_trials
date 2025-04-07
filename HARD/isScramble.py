'''
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

 

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now, and the result string is "rgeat" which is s2.
As one possible scenario led s1 to be scrambled to s2, we return true.
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
Example 3:

Input: s1 = "a", s2 = "a"
Output: true
'''

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        memo = {}
        
        def helper(a, b):
            if a == b:
                return True
            if (a, b) in memo:
                return memo[(a, b)]
            # If the sorted characters are not the same, then b can't be a scramble of a.
            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False
            
            n = len(a)
            # Try every possible split
            for i in range(1, n):
                # Case 1: No swap between the substrings.
                if helper(a[:i], b[:i]) and helper(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                # Case 2: Substrings swapped.
                if helper(a[:i], b[-i:]) and helper(a[i:], b[:-i]):
                    memo[(a, b)] = True
                    return True
            
            memo[(a, b)] = False
            return False
        
        return helper(s1, s2)

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    # Example 1:
    s1 = "great"
    s2 = "rgeat"
    print("Is '{}' a scramble of '{}'? -> {}".format(s2, s1, sol.isScramble(s1, s2)))
    
    # Example 2:
    s1 = "abcde"
    s2 = "caebd"
    print("Is '{}' a scramble of '{}'? -> {}".format(s2, s1, sol.isScramble(s1, s2)))
    
    # Example 3:
    s1 = "a"
    s2 = "a"
    print("Is '{}' a scramble of '{}'? -> {}".format(s2, s1, sol.isScramble(s1, s2)))
