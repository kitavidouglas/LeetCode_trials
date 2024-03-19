def reverseBits(n):
    result = 0
    # Iterate through each bit of the input integer
    for _ in range(32):
        # Shift the result to the left to make space for the next bit
        result <<= 1
        # Get the least significant bit of n and append it to the result
        result |= n & 1
        # Right-shift n to process the next bit
        n >>= 1
    return result

# Example usage
n = 0b00000010100101000001111010011100
print(reverseBits(n))  # Output: 964176192 (0b00111001011110000010100101000000)
