class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

# Test cases
solutions = Solution()
print(solutions.isValid("()"))         # Output: True
print(solutions.isValid("()[]{}"))     # Output: True
print(solutions.isValid("(]"))         # Output: False
print(solutions.isValid("([)]"))       # Output: False
print(solutions.isValid("{[]}"))       # Output: True
