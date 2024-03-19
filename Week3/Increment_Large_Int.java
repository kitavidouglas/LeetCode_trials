package Week3;

import java.util.Arrays;

public class Increment_Large_Int {
    public static int[] plusOne(int[] digits) {
        int n = digits.length;
        int carry = 1;

        // Iterate through the digits array from right to left
        for (int i = n - 1; i >= 0; i--) {
            digits[i] += carry;
            if (digits[i] == 10) {
                digits[i] = 0;
                carry = 1;
            } else {
                carry = 0;
                break;
            }
        }

        // If there's still a carry after processing all digits, add an extra leading 1 to the array
        if (carry == 1) {
            int[] result = new int[n + 1];
            result[0] = 1;
            return result;
        }

        return digits;
    }

    public static void main(String[] args) {
        int[] digits = {1, 2, 3};
        System.out.println(Arrays.toString(plusOne(digits))); // Output: [1, 2, 4]
    }
}
