public class Day5 {
    public static boolean isPalindrome(int x) {
        // If x is negative, it cannot be a palindrome
        if (x < 0) {
            return false;
        }

        int original = x;
        int reversed = 0;

        // Reverse the number
        while (x != 0) {
            int digit = x % 10;
            reversed = reversed * 10 + digit;
            x /= 10;
        }

        // Check if the original number equals the reversed number
        return original == reversed;
    }

    public static void main(String[] args) {
        int num1 = 121;
        int num2 = -121;

        System.out.println("Is " + num1 + " a palindrome? " + isPalindrome(num1)); // Output: true
        System.out.println("Is " + num2 + " a palindrome? " + isPalindrome(num2)); // Output: false
    }
}
