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

import heapq

class NumberContainers(object):

    def __init__(self):
        self.index_to_number = {}  # Maps index -> number
        self.number_to_indices = {}  # Maps number -> min-heap of indices

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number in self.number_to_indices:
                self.number_to_indices[old_number].discard(index)  # Remove from old number's set

        # Assign the new number to the index
        self.index_to_number[index] = number
        if number not in self.number_to_indices:
            self.number_to_indices[number] = set()
        
        self.number_to_indices[number].add(index)

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number not in self.number_to_indices or not self.number_to_indices[number]:
            return -1
        return min(self.number_to_indices[number])

import heapq

class NumberContainers(object):

    def __init__(self):
        self.index_to_number = {}  # Maps index -> number
        self.number_to_indices = {}  # Maps number -> min-heap of indices

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number in self.number_to_indices:
                self.number_to_indices[old_number].discard(index)  # Remove from old number's set

        # Assign the new number to the index
        self.index_to_number[index] = number
        if number not in self.number_to_indices:
            self.number_to_indices[number] = set()
        
        self.number_to_indices[number].add(index)

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number not in self.number_to_indices or not self.number_to_indices[number]:
            return -1
        return min(self.number_to_indices[number])

import heapq

class NumberContainers(object):

    def __init__(self):
        self.index_to_number = {}  # Maps index -> number
        self.number_to_indices = {}  # Maps number -> min-heap of indices

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number in self.number_to_indices:
                self.number_to_indices[old_number].discard(index)  # Remove from old number's set

        # Assign the new number to the index
        self.index_to_number[index] = number
        if number not in self.number_to_indices:
            self.number_to_indices[number] = set()
        
        self.number_to_indices[number].add(index)

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number not in self.number_to_indices or not self.number_to_indices[number]:
            return -1
        return min(self.number_to_indices[number])
'''In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

'''

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = {}  # Dictionary to store the parent of each node
        
        def find(x):
            """Finds the root of the node using path compression."""
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            """Unites two sets and returns False if they are already connected."""
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False  # Cycle detected
            parent[rootY] = rootX  # Union the sets
            return True
        
        # Initialize the parent dictionary
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            if not union(u, v):  # If union returns False, this edge is redundant
                return [u, v]

# Example usage:
solution = Solution()
print(solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # Output: [2, 3]
print(solution.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # Output: [1, 4]

'''In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

'''

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = {}  # Dictionary to store the parent of each node
        
        def find(x):
            """Finds the root of the node using path compression."""
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            """Unites two sets and returns False if they are already connected."""
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False  # Cycle detected
            parent[rootY] = rootX  # Union the sets
            return True
        
        # Initialize the parent dictionary
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            if not union(u, v):  # If union returns False, this edge is redundant
                return [u, v]

# Example usage:
solution = Solution()
print(solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # Output: [2, 3]
print(solution.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # Output: [1, 4]

'''In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

'''

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = {}  # Dictionary to store the parent of each node
        
        def find(x):
            """Finds the root of the node using path compression."""
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            """Unites two sets and returns False if they are already connected."""
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False  # Cycle detected
            parent[rootY] = rootX  # Union the sets
            return True
        
        # Initialize the parent dictionary
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            if not union(u, v):  # If union returns False, this edge is redundant
                return [u, v]

# Example usage:
solution = Solution()
print(solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # Output: [2, 3]
print(solution.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # Output: [1, 4]

'''In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

'''

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = {}  # Dictionary to store the parent of each node
        
        def find(x):
            """Finds the root of the node using path compression."""
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            """Unites two sets and returns False if they are already connected."""
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False  # Cycle detected
            parent[rootY] = rootX  # Union the sets
            return True
        
        # Initialize the parent dictionary
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            if not union(u, v):  # If union returns False, this edge is redundant
                return [u, v]

# Example usage:
solution = Solution()
print(solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # Output: [2, 3]
print(solution.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # Output: [1, 4]

'''In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

'''

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = {}  # Dictionary to store the parent of each node
        
        def find(x):
            """Finds the root of the node using path compression."""
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            """Unites two sets and returns False if they are already connected."""
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False  # Cycle detected
            parent[rootY] = rootX  # Union the sets
            return True
        
        # Initialize the parent dictionary
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            if not union(u, v):  # If union returns False, this edge is redundant
                return [u, v]

# Example usage:
solution = Solution()
print(solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # Output: [2, 3]
print(solution.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # Output: [1, 4]

'''In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

'''

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = {}  # Dictionary to store the parent of each node
        
        def find(x):
            """Finds the root of the node using path compression."""
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            """Unites two sets and returns False if they are already connected."""
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False  # Cycle detected
            parent[rootY] = rootX  # Union the sets
            return True
        
        # Initialize the parent dictionary
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            if not union(u, v):  # If union returns False, this edge is redundant
                return [u, v]

# Example usage:
solution = Solution()
print(solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # Output: [2, 3]
print(solution.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # Output: [1, 4]

'''In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

'''

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = {}  # Dictionary to store the parent of each node
        
        def find(x):
            """Finds the root of the node using path compression."""
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            """Unites two sets and returns False if they are already connected."""
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False  # Cycle detected
            parent[rootY] = rootX  # Union the sets
            return True
        
        # Initialize the parent dictionary
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            if not union(u, v):  # If union returns False, this edge is redundant
                return [u, v]

# Example usage:
solution = Solution()
print(solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # Output: [2, 3]
print(solution.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # Output: [1, 4]

'''In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

'''

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = {}  # Dictionary to store the parent of each node
        
        def find(x):
            """Finds the root of the node using path compression."""
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            """Unites two sets and returns False if they are already connected."""
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False  # Cycle detected
            parent[rootY] = rootX  # Union the sets
            return True
        
        # Initialize the parent dictionary
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            if not union(u, v):  # If union returns False, this edge is redundant
                return [u, v]

# Example usage:
solution = Solution()
print(solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # Output: [2, 3]
print(solution.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # Output: [1, 4]

