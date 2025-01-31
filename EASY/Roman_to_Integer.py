''' Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer

'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0  # Track the previous numeral's value
        
        for char in reversed(s):  # Process from right to left
            curr_value = roman_values[char]
            
            if curr_value < prev_value:
                total -= curr_value  # Subtraction case
            else:
                total += curr_value  # Addition case
            
            prev_value = curr_value  # Update previous value
        
        return total

# Sample main function for testing
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
    
    for s in test_cases:
        print(f"Roman: {s}, Integer: {solution.romanToInt(s)}")

