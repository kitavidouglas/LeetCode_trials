package Week5;

public class Sqrt {
    public static int sqrt(int x) {
        // Handle base cases
        if (x == 0 || x == 1) {
            return x;
        }

        // Initialize left and right pointers for binary search
        int left = 1;
        int right = x;

        // Perform binary search
        while (left <= right) {
            int mid = left + (right - left) / 2;

            // Check if mid^2 is the target
            if (mid == x / mid) {
                return mid;
            }

            // If mid^2 is greater than x, search left half
            else if (mid > x / mid) {
                right = mid - 1;
            }

            // If mid^2 is less than x, search right half
            else {
                left = mid + 1;
            }
        }

        // At this point, left will be the floor value of the square root
        return left - 1;
    }

    public static void main(String[] args) {
        int x = 4;
        System.out.println(sqrt(x));  // Output: 2
    }
}
