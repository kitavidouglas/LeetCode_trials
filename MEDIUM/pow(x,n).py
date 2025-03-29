'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104

'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1  # Base case: Any number raised to power 0 is 1
        
        if n < 0:
            x = 1 / x
            n = -n  # Convert negative exponent to positive for computation
        
        result = 1
        while n > 0:
            if n % 2 == 1:  # If n is odd, multiply result by x
                result *= x
            x *= x  # Square the base
            n //= 2  # Reduce exponent by half
        
        return result

