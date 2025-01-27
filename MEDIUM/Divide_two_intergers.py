#Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

#The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

#Return the quotient after dividing dividend by divisor.

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Edge case: handle overflow for 32-bit signed integer range
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # Max 32-bit integer value

        # Determine the sign of the result
        sign = -1 if (dividend < 0) != (divisor < 0) else 1

        # Work with absolute values to avoid handling negative signs during division
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        # Repeatedly subtract divisor from dividend using bit shifts
        while dividend >= divisor:
            temp_divisor, num_divisors = divisor, 1
            # Double the divisor until it's greater than the dividend
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_divisors <<= 1
            
            # Subtract the multiple of the divisor from dividend and add to quotient
            dividend -= temp_divisor
            quotient += num_divisors
        
        # Apply the sign to the quotient
        quotient *= sign

        # Return the quotient within the 32-bit integer range
        return max(-2**31, min(quotient, 2**31 - 1))

# Sample main function to compute sample values
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Regular division
    dividend = 10
    divisor = 3
    print(f"Dividend: {dividend}, Divisor: {divisor} => Result: {solution.divide(dividend, divisor)}")

    # Test case 2: Negative dividend
    dividend = -10
    divisor = 3
    print(f"Dividend: {dividend}, Divisor: {divisor} => Result: {solution.divide(dividend, divisor)}")

    # Test case 3: Negative divisor
    dividend = 10
    divisor = -3
    print(f"Dividend: {dividend}, Divisor: {divisor} => Result: {solution.divide(dividend, divisor)}")

    # Test case 4: Both negative
    dividend = -10
    divisor = -3
    print(f"Dividend: {dividend}, Divisor: {divisor} => Result: {solution.divide(dividend, divisor)}")

    # Test case 5: Edge case where result is beyond 32-bit integer range
    dividend = -2**31
    divisor = -1
    print(f"Dividend: {dividend}, Divisor: {divisor} => Result: {solution.divide(dividend, divisor)}")
