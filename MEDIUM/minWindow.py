'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        
        if not t or not s:
            return ""
        
        # Count of chars we need in the window
        need = Counter(t)
        required = len(need)   # number of distinct chars in t to be satisfied
        
        # Sliding window pointers and formed count
        l = 0
        formed = 0
        window_counts = {}
        
        # (window length, left, right)
        ans = float("inf"), None, None
        
        # Expand the window with r
        for r, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # If this char now satisfies the need for that char, increment formed
            if char in need and window_counts[char] == need[char]:
                formed += 1
            
            # Try to contract the window until it stops being 'desirable'
            while l <= r and formed == required:
                # Update best answer
                if (r - l + 1) < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # Remove from window_counts and possibly update formed
                left_char = s[l]
                window_counts[left_char] -= 1
                if left_char in need and window_counts[left_char] < need[left_char]:
                    formed -= 1
                
                l += 1  # shrink from the left
        
        # Return the smallest window, or "" if no valid window was found
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
