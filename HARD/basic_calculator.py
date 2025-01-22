#Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

#Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        sign = 1  # 1 means positive, -1 means negative
        result = 0
        
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)  # Build the number from digits
            elif char == '+':
                result += sign * num  # Apply the last operator
                num = 0  # Reset num for the next number
                sign = 1  # Set the sign to positive for the next number
            elif char == '-':
                result += sign * num  # Apply the last operator
                num = 0  # Reset num for the next number
                sign = -1  # Set the sign to negative for the next number
            elif char == '(':
                # Push the current result and sign onto the stack and reset
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * num  # Apply the last operator
                num = 0  # Reset num
                result *= stack.pop()  # Pop the sign from the stack
                result += stack.pop()  # Pop the last result from the stack

        # Finally, apply the last number in num
        result += sign * num
        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s1 = "1 + 1"
    print(f"Result of '{s1}':", solution.calculate(s1))  # Output: 2

    # Example 2
    s2 = " 2-1 + 2 "
    print(f"Result of '{s2}':", solution.calculate(s2))  # Output: 3

    # Example 3
    s3 = "(1+(4+5+2)-3)+(6+8)"
    print(f"Result of '{s3}':", solution.calculate(s3))  # Output: 23
