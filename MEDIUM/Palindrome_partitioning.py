#Given a string s, partition s such that every substring of the partition is a palindrome
#Return all possible palindrome partitioning of s.



class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        def is_palindrome(substring):
            return substring == substring[::-1]

        def backtrack(start, current_partition):
            # Base case: if we've used the entire string, add the partition to results
            if start == len(s):
                result.append(current_partition[:])
                return

            # Try all possible substrings starting from the 'start' index
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    # If substring is a palindrome, add it to the current partition and recurse
                    current_partition.append(substring)
                    backtrack(end, current_partition)
                    current_partition.pop()  # Backtrack

        result = []
        backtrack(0, [])
        return result

# Sample main function to compute sample values
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Palindrome partitions of the string "aab"
    s = "aab"
    print(f"Palindrome partitions of '{s}': {solution.partition(s)}")

    # Test case 2: Palindrome partitions of the string "a"
    s = "a"
    print(f"Palindrome partitions of '{s}': {solution.partition(s)}")

    # Test case 3: Palindrome partitions of the string "racecar"
    s = "racecar"
    print(f"Palindrome partitions of '{s}': {solution.partition(s)}")

    # Test case 4: Palindrome partitions of an empty string
    s = ""
    print(f"Palindrome partitions of '{s}': {solution.partition(s)}")






