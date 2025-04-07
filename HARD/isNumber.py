'''
Given a string s, return whether s is a valid number.

For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

Formally, a valid number is defined using one of the following definitions:

An integer number followed by an optional exponent.
A decimal number followed by an optional exponent.
An integer number is defined with an optional sign '-' or '+' followed by digits.

A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

Digits followed by a dot '.'.
Digits followed by a dot '.' followed by digits.
A dot '.' followed by digits.
An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

The digits are defined as one or more digits.

 

Example 1:

Input: s = "0"

Output: true

Example 2:

Input: s = "e"

Output: false


'''
import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Remove leading/trailing whitespace
        s = s.strip()
        # Regular expression pattern to match a valid number.
        # Breakdown:
        # ^[+-]?                     -> Optional sign at the beginning.
        # (                          -> Start group for the number part.
        #    (\d+(\.\d*)?)          -> Option 1: digits followed by an optional dot with optional digits.
        #    |                      -> OR
        #    (\.\d+)                -> Option 2: a dot followed by digits.
        # )
        # ([eE][+-]?\d+)?            -> Optional exponent part: 'e' or 'E' followed by an optional sign and digits.
        # $                          -> End of string.
        pattern = re.compile(r'^[+-]?((\d+(\.\d*)?)|(\.\d+))([eE][+-]?\d+)?$')
        return bool(pattern.match(s))

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "2", "0089", "-0.1", "+3.14", "4.", "-.9",
        "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789",
        "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"
    ]
    
    for s in test_cases:
        print("Input:", s, "->", sol.isNumber(s))
