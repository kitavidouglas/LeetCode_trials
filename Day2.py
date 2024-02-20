def length_of_last_word(s: str) -> int:
    # Split the string into words
    words = s.split()

    # Trim the list of words
    while words and words[-1] == '':
        words.pop()

    # If there are no words left after trimming, return 0
    if not words:
        return 0

    # Retrieve the last word
    last_word = words[-1]

    # Return the length of the last word
    return len(last_word)

# Test the function
if __name__ == "__main__":
    input_string = input("Enter a string with words and spaces: ")
    print("Length of the last word:", length_of_last_word(input_string))

