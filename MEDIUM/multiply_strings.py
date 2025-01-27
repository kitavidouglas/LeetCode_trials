#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

#Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Edge case: if any number is zero, return "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize result array of size len(num1) + len(num2)
        result = [0] * (len(num1) + len(num2))
        
        # Reverse both numbers to make multiplication easier
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        # Perform the multiplication
        for i in range(len(num1)):
            for j in range(len(num2)):
                # Multiply the digits and add to the current position
                product = int(num1[i]) * int(num2[j])
                result[i + j] += product
                # Handle the carry for the current position
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        # Remove any leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        # Convert result array to string
        return ''.join(map(str, result[::-1]))

# Sample main function to compute sample values
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Multiply two positive numbers
    num1 = "123"
    num2 = "456"
    print(f"Multiplying {num1} and {num2} gives: {solution.multiply(num1, num2)}")

    # Test case 2: Multiply a number by zero
    num1 = "0"
    num2 = "456"
    print(f"Multiplying {num1} and {num2} gives: {solution.multiply(num1, num2)}")

    # Test case 3: Multiply a number by one
    num1 = "123"
    num2 = "1"
    print(f"Multiplying {num1} and {num2} gives: {solution.multiply(num1, num2)}")

    # Test case 4: Multiply two large numbers
    num1 = "987654321"
    num2 = "123456789"
    print(f"Multiplying {num1} and {num2} gives: {solution.multiply(num1, num2)}")
