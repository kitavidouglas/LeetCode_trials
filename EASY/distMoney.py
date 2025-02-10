''' You are given an integer money denoting the amount of money (in dollars) that you have and another integer children denoting the number of children that you must distribute the money to.

You have to distribute the money according to the following rules:

All money must be distributed.
Everyone must receive at least 1 dollar.
Nobody receives 4 dollars.
Return the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the aforementioned rules. If there is no way to distribute the money, return -1.

 

Example 1:

Input: money = 20, children = 3
Output: 1
Explanation: 
The maximum number of children with 8 dollars will be 1. One of the ways to distribute the money is:
- 8 dollars to the first child.
- 9 dollars to the second child. 
- 3 dollars to the third child.
It can be proven that no distribution exists such that number of children getting 8 dollars is greater than 1.
Example 2:

Input: money = 16, children = 2
Output: 2
Explanation: Each child can be given 8 dollars.

'''


class Solution(object):
    def distMoney(self, money, children):
        """
        :type money: int
        :type children: int
        :rtype: int
        """
        # Check if it's possible to distribute money fairly
        if money < children:
            return -1  # Not enough money to give at least $1 to each child
        
        money -= children  # Give each child $1 initially
        max_eight_dollar_children = min(money // 7, children)  # Maximum kids who can get $8
        
        money -= max_eight_dollar_children * 7  # Deduct the allocated $8
        
        if max_eight_dollar_children == children and money > 0:
            return children - 1  # Adjust if extra money remains
        
        if money == 3 and max_eight_dollar_children == children - 1:
            return children - 2  # Avoid giving exactly $4 to one child
        
        return max_eight_dollar_children
