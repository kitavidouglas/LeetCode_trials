def roman_to_int(s: str) -> int:
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0
    for char in s:
        value = roman_values.get(char)
        if value is None:
            return -1  # Invalid Roman numeral
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value
    return total

# Test the function
roman_numeral = input("Enter a Roman numeral: ").upper()
result = roman_to_int(roman_numeral)
if result != -1:
    print(f"The integer value of {roman_numeral} is: {result}")
else:
    print("Invalid Roman numeral entered!")
