class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Step 1: Compute the prefix sum array
        n = len(words)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
        
        # Step 2: Answer queries in O(1) time
        ans = []
        for li, ri in queries:
            ans.append(prefix[ri + 1] - prefix[li])
        
        return ans
