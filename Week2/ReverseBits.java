package Week2;

public class ReverseBits {
    public int reverseBits(int n) {
        int result = 0;
        // Iterate through each bit of the input integer
        for (int i = 0; i < 32; i++) {
            // Shift the result to the left to make space for the next bit
            result <<= 1;
            // Get the least significant bit of n and append it to the result
            result |= n & 1;
            // Right-shift n to process the next bit
            n >>>= 1; // Use logical right shift to handle unsigned integers
        }
        return result;
    }

    public static void main(String[] args) {
        ReverseBits solution = new ReverseBits();

        // Example usage
        int n = 0b00000010100101000001111010011100;
        System.out.println(solution.reverseBits(n));  // Output: 964176192 (0b00111001011110000010100101000000)
    }
}
