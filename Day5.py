class PalindromeChecker:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        # If x is negative, it cannot be a palindrome
        if x < 0:
            return False

        original = x
        reversed_num = 0

        # Reverse the number
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        # Check if the original number equals the reversed number
        return original == reversed_num


if __name__ == "__main__":
    num1 = 121
    num2 = -121

    print(f"Is {num1} a palindrome? {PalindromeChecker.isPalindrome(num1)}")  # Output: True
    print(f"Is {num2} a palindrome? {PalindromeChecker.isPalindrome(num2)}")  # Output: False
