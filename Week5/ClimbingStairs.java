package Week5;
public class ClimbingStairs {
    public static int climbStairs(int n) {
        // Base cases
        if (n == 0) {
            return 1; // There is 1 way to climb 0 steps (do nothing)
        }
        if (n < 0) {
            return 0; // If we overshoot the top, there are no ways
        }

        // Initialize variables to store the number of ways for the last two steps
        int prev1 = 1; // Number of ways to climb 1 step
        int prev2 = 1; // Number of ways to climb 0 steps (base case)

        // Calculate the number of ways for each step
        for (int i = 2; i <= n; i++) {
            int current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
        }

        // Return the number of ways to reach the top
        return prev1;
    }

    public static void main(String[] args) {
        int n = 2;
        System.out.println(climbStairs(n)); // Output: 2
    }
}
