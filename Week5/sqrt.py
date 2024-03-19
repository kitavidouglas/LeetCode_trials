def sqrt(x):
    # Handle base cases
    if x == 0 or x == 1:
        return x

    # Initialize left and right pointers for binary search
    left = 1
    right = x

    # Perform binary search
    while left <= right:
        mid = (left + right) // 2

        # Check if mid^2 is the target
        if mid * mid == x:
            return mid

        # If mid^2 is greater than x, search left half
        elif mid * mid > x:
            right = mid - 1

        # If mid^2 is less than x, search right half
        else:
            left = mid + 1

    # At this point, left will be the floor value of the square root
    return left - 1

# Example usage
x = 4
print(sqrt(x))  # Output: 2
