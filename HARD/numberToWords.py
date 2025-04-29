'''
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 231 - 1
'''

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        
        # Words for numbers less than 20
        below20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine",
                   "Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen",
                   "Sixteen","Seventeen","Eighteen","Nineteen"]
        
        # Words for tens multiples from 20 to 90
        tens = ["","", "Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        
        # Scale words for each thousand-power
        thousands = ["","Thousand","Million","Billion"]
        
        def three_digits_to_words(n):
            """Convert a number 0 <= n < 1000 to English words (no trailing spaces)."""
            if n == 0:
                return ""
            elif n < 20:
                return below20[n]
            elif n < 100:
                t = n // 10
                rest = n % 10
                return tens[t] + (" " + below20[rest] if rest else "")
            else:
                h = n // 100
                rest = n % 100
                return below20[h] + " Hundred" + (" " + three_digits_to_words(rest) if rest else "")
        
        res_parts = []
        chunk_index = 0
        
        # Process the number in chunks of 3 digits, from lowest to highest
        while num > 0:
            chunk = num % 1000
            if chunk:
                words = three_digits_to_words(chunk)
                scale = thousands[chunk_index]
                # Add the chunk’s words plus its scale (if not the units chunk)
                res_parts.append(words + (" " + scale if scale else ""))
            num //= 1000
            chunk_index += 1
        
        # Since we built parts from low to high, reverse and join
        return " ".join(res_parts[::-1])
