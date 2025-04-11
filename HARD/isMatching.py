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
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        # dp[i][j] will be True if s[i:] matches p[j:].
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty pattern matches empty string
        dp[m][n] = True
        
        # Fill table bottom-up
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                # Check if first character matches (and we’re not past the end of s)
                first_match = (i < m) and (p[j] == s[i] or p[j] == '.')
                
                # Handle '*' as "zero or more of preceding element"
                if j + 1 < n and p[j+1] == '*':
                    # Two cases:
                    # 1) We treat "x*" as matching zero of x: skip p[j] and '*' → dp[i][j+2]
                    # 2) If first_match, consume one s character and stay on the same pattern → dp[i+1][j]
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    # No '*' follows: must match this char and then the rest
                    dp[i][j] = first_match and dp[i+1][j+1]
        
        return dp[0][0]
