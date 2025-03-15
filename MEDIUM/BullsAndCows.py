class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows = 0
        secret_count = {}
        guess_count = {}
        
        # First pass: count bulls and record frequencies of unmatched digits
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[s] = secret_count.get(s, 0) + 1
                guess_count[g] = guess_count.get(g, 0) + 1
        
        # Second pass: count cows by comparing frequency counts
        for digit in secret_count:
            if digit in guess_count:
                cows += min(secret_count[digit], guess_count[digit])
                
        return "{}A{}B".format(bulls, cows)
