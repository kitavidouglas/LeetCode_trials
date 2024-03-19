def maxProfit(prices):
    if not prices:
        return 0
    
    # Initialize minimum price and maximum profit
    min_price = prices[0]
    max_profit = 0
    
    # Iterate through prices
    for price in prices:
        # Update minimum price if current price is lower
        min_price = min(min_price, price)
        # Update maximum profit if current price allows higher profit
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5
