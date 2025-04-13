from collections import Counter
'''
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].
'''
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        n = len(s)
        
        # frequency map of the words we need
        target = Counter(words)
        res = []
        
        # We only need to scan with word_len different offsets
        for offset in range(word_len):
            left = offset            # start of our window
            curr_count = Counter()   # counts of words in the current window
            count = 0                # how many valid words we've matched
            
            # Move in steps of word_len
            for right in range(offset, n - word_len + 1, word_len):
                w = s[right:right + word_len]
                
                # If it's one of the words we want, include it
                if w in target:
                    curr_count[w] += 1
                    count += 1
                    
                    # If we've seen this word too many times, shrink from the left
                    while curr_count[w] > target[w]:
                        left_w = s[left:left + word_len]
                        curr_count[left_w] -= 1
                        left += word_len
                        count -= 1
                    
                    # If we've matched exactly num_words words, record the start
                    if count == num_words:
                        res.append(left)
                        
                        # Then slide forward by one word to look for the next match
                        left_w = s[left:left + word_len]
                        curr_count[left_w] -= 1
                        left += word_len
                        count -= 1
                else:
                    # Reset the window
                    curr_count.clear()
                    count = 0
                    left = right + word_len
        
        return res
