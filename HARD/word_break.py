#Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word.
# Return all such possible sentences in any order.


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # Create a set for faster lookup of words
        wordSet = set(wordDict)
        
        # Dictionary for memoization
        memo = {}

        def backtrack(start):
            # If we reach the end of the string, return an empty list to form sentences
            if start == len(s):
                return [""]

            # If the result for this start index is already calculated, return it
            if start in memo:
                return memo[start]

            sentences = []

            # Try every possible end index for substrings starting from `start`
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    # Recursively get all possible sentences from the remaining substring
                    remaining_sentences = backtrack(end)
                    for sentence in remaining_sentences:
                        if sentence:
                            sentences.append(word + " " + sentence)
                        else:
                            sentences.append(word)
            
            # Store the result in the memoization dictionary
            memo[start] = sentences
            return sentences

        return backtrack(0)


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s1 = "catsanddog"
    wordDict1 = ["cat", "cats", "and", "sand", "dog"]
    print("Possible sentences for 'catsanddog':", solution.wordBreak(s1, wordDict1))

    # Example 2
    s2 = "pineapplepenapple"
    wordDict2 = ["apple", "pen", "applepen", "pine", "pineapple"]
    print("Possible sentences for 'pineapplepenapple':", solution.wordBreak(s2, wordDict2))

    # Example 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    print("Possible sentences for 'catsandog':", solution.wordBreak(s3, wordDict3))

