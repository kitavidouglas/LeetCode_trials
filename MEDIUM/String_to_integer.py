''' Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.  '''

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1  # Maximum 32-bit signed integer
        INT_MIN = -2**31      # Minimum 32-bit signed integer
        
        i = 0
        n = len(s)
        sign = 1  # Default positive sign
        result = 0

        # Step 1: Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Check for sign
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 3: Read digits and convert to integer
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow before adding the digit
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1
        
        return sign * result

# Example usage:
solution = Solution()
print(solution.myAtoi("42"))       # Output: 42
print(solution.myAtoi("   -042"))  # Output: -42
print(solution.myAtoi("4193 with words"))  # Output: 4193
print(solution.myAtoi("words and 987"))   # Output: 0
print(solution.myAtoi("-91283472332"))    # Output: -2147483648 (clamped)
