"""The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
"""


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1  # Convert k to 0-indexed
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Pre-calculate factorials up to n
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i
        
        result = []
        for i in range(n, 0, -1):
            # Determine the index of the next number to append
            index = k // factorial[i - 1]
            k %= factorial[i - 1]
            result.append(numbers[index])
            numbers.pop(index)
            
        return ''.join(result)
