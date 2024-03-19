package Week2;

public class FindComplement {
    public int findComplement(int num) {
        // Count the number of significant bits
        int significantBits = 0;
        int n = num;
        while (n > 0) {
            significantBits++;
            n >>= 1;
        }
        
        // Create a bitmask with all significant bits set to 1
        int bitmask = (1 << significantBits) - 1;
        
        // Return the complement of num
        return num ^ bitmask;
    }

    public static void main(String[] args) {
        FindComplement solution = new FindComplement();
        
        // Example usage
        System.out.println(solution.findComplement(5));  // Output: 2
        System.out.println(solution.findComplement(1));  // Output: 0
    }
}
