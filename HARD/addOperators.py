'''
Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

 

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
Example 3:

Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
 

Constraints:

1 <= num.length <= 10
num consists of only digits.
-231 <= target <= 231 - 1

'''

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # Result list
        res = []
        n = len(num)
        if n == 0:
            return res

        def backtrack(expr, pos, prev, total):
            """
            expr  : current expression string
            pos   : next index in num to consume
            prev  : last operand's value (signed)
            total : current evaluated total of expr
            """
            # If we've used all digits, check if we hit target
            if pos == n:
                if total == target:
                    res.append(expr)
                return

            # Try all splits num[pos:i+1]
            for i in range(pos, n):
                # Skip numbers with leading zero
                if i > pos and num[pos] == '0':
                    break

                curr_str = num[pos:i+1]
                curr = int(curr_str)

                if pos == 0:
                    # First number, we can't add an operator before it
                    backtrack(curr_str, i+1, curr, curr)
                else:
                    # +
                    backtrack(expr + '+' + curr_str, i+1,  curr, total + curr)
                    # -
                    backtrack(expr + '-' + curr_str, i+1, -curr, total - curr)
                    # *
                    # Remove prev from total, add prev * curr
                    backtrack(expr + '*' + curr_str,
                              i+1,
                              prev * curr,
                              total - prev + prev * curr)

        backtrack("", 0, 0, 0)
        return res
