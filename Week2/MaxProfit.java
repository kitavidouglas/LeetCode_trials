package Week2;

public class MaxProfit {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length == 0) {
            return 0;
        }

        // Initialize minimum price and maximum profit
        int minPrice = prices[0];
        int maxProfit = 0;

        // Iterate through prices
        for (int i = 1; i < prices.length; i++) {
            // Update minimum price if current price is lower
            minPrice = Math.min(minPrice, prices[i]);
            // Update maximum profit if current price allows higher profit
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
        }

        return maxProfit;
    }

    public static void main(String[] args) {
        MaxProfit solution = new MaxProfit();

        // Example usage
        int[] prices = {7, 1, 5, 3, 6, 4};
        System.out.println(solution.maxProfit(prices)); // Output: 5
    }
}
