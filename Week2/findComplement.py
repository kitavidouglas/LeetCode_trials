def findComplement(num):
    # Count the number of significant bits
    significant_bits = 0
    n = num
    while n > 0:
        significant_bits += 1
        n >>= 1
    
    # Create a bitmask with all significant bits set to 1
    bitmask = (1 << significant_bits) - 1
    
    # Return the complement of num
    return num ^ bitmask

# Example usage
print(findComplement(5))  # Output: 2
print(findComplement(1))  # Output: 0
