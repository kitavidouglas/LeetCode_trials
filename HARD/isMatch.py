'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        
        def dp(i, j):
            # Check if result is already computed.
            if (i, j) in memo:
                return memo[(i, j)]
            
            # If we've reached the end of the pattern, s must also be exhausted.
            if j == len(p):
                return i == len(s)
            
            # Check if current characters match (considering '.')
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            
            # Handle '*' in the pattern.
            if j + 1 < len(p) and p[j+1] == '*':
                # Two cases:
                # 1. Skip the "character*"
                # 2. If current characters match, move forward in s keeping the same pattern.
                ans = dp(i, j+2) or (first_match and dp(i+1, j))
            else:
                # Move forward if current characters match.
                ans = first_match and dp(i+1, j+1)
            
            memo[(i, j)] = ans
            return ans
        
        return dp(0, 0)
