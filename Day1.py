class MinOperationsToMakeEqualStrings:
    def min_operations(self, s1: str, s2: str, s3: str) -> int:
        len1, len2, len3 = len(s1), len(s2), len(s3)
        max_len = max(len1, len2, len3)
        
        # Pad the strings with spaces to make their lengths equal
        s1 = self.pad_string(s1, max_len)
        s2 = self.pad_string(s2, max_len)
        s3 = self.pad_string(s3, max_len)
        
        operations = 0
        for i in range(max_len - 1, -1, -1):
            c1, c2, c3 = s1[i], s2[i], s3[i]
            
            # If all characters are equal, continue to the next character
            if c1 == c2 == c3:
                continue
            
            # If any character is different, increment the operations count
            operations += 1
            
            # If any string is already empty, return -1
            if c1 == ' ' or c2 == ' ' or c3 == ' ':
                return -1
            
            # Otherwise, delete the rightmost character of the longest string
            if len1 == max_len:
                s1 = s1[:i]
            elif len2 == max_len:
                s2 = s2[:i]
            else:
                s3 = s3[:i]
        
        return operations
    
    # Pad the string with spaces to make its length equal to max_len
    def pad_string(self, s: str, max_len: int) -> str:
        return s.ljust(max_len)

# Example usage:
solution = MinOperationsToMakeEqualStrings()
s1 = "abcttt"
s2 = "abcddo"
s3 = "abcduu"
print(solution.min_operations(s1, s2, s3))  # Output: 1
