class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        start, end = 0, 0  # bounds of the best palindrome found
        
        for i in range(len(s)):
            # Odd-length palindromes, center at i
            len1 = self._expand(s, i, i)
            # Even-length palindromes, center between i and i+1
            len2 = self._expand(s, i, i+1)
            
            max_len = max(len1, len2)
            if max_len > end - start + 1:
                # Recompute the new start/end from i and max_len
                # For odd: start = i - (max_len-1)//2, end = i + (max_len-1)//2
                # For even: start = i - (max_len//2 - 1), end = i + max_len//2
                start = i - (max_len - 1) // 2
                end   = i + max_len // 2
        
        return s[start:end+1]
    
    def _expand(self, s, left, right):
        """
        Expand around the center [left,right] as long as s[left]==s[right].
        Return the length of the palindrome.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left  -= 1
            right += 1
        # When the loop breaks, [left+1 .. right-1] is the maximal palindrome
        return right - left - 1
