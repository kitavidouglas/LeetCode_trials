def plusOne(digits):
    n = len(digits)
    carry = 1

    for i in range(n - 1, -1, -1):
        digits[i] += carry
        if digits[i] == 10:
            digits[i] = 0
            carry = 1
        else:
            carry = 0
            break
    
    if carry:
        digits.insert(0, 1)
    
    return digits

# Example usage
digits = [1, 2, 3]
print(plusOne(digits))  # Output: [1, 2, 4]
