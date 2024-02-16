def min_operations(s1: str, s2: str, s3: str) -> int:
    operations = 0
    
    while s1 != s2 or s2 != s3:
        if not s1 or not s2 or not s3:
            return -1
        
        max_len = max(len(s1), len(s2), len(s3))
        
        if len(s1) == max_len:
            s1 = s1[:-1]
        elif len(s2) == max_len:
            s2 = s2[:-1]
        else:
            s3 = s3[:-1]
        
        operations += 1
    
    return operations

# Input from the user
s1 = input("Enter string s1: ")
s2 = input("Enter string s2: ")
s3 = input("Enter string s3: ")

# Calculate and print the minimum number of operations
min_ops = min_operations(s1, s2, s3)
print("Minimum operations needed:", min_ops)
