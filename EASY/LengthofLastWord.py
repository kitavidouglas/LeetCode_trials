''' Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
 '''

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split()[-1])  # Strip spaces, split into words, and get the last word's length

# Sample main function for testing
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        "Hello World", 
        "   fly me   to   the moon  ", 
        "a", 
        "   space    ", 
        "trailingSpaces    "
    ]
    
    for s in test_cases:
        print(f"Input: '{s}' | Length of Last Word: {solution.lengthOfLastWord(s)}")
