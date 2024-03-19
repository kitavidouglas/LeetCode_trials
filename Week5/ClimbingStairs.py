def climbStairs(n):
    # Base cases
    if n == 0:
        return 1  # There is 1 way to climb 0 steps (do nothing)
    if n < 0:
        return 0  # If we overshoot the top, there are no ways
    
    # Initialize an array to store the number of ways for each step
    dp = [0] * (n + 1)
    # Base cases: there is 1 way to climb 0 steps
    dp[0] = 1
    dp[1] = 1
    
    # Calculate the number of ways for each step
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    # Return the number of ways to reach the top
    return dp[n]

# Example usage
n = 2
print(climbStairs(n))  # Output: 2
