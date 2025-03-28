# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

 

Example 1:


Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:


Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
Example 3:


Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]

'''
class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: Optional[TreeNode]
        """
        # Initialize the index for parsing the traversal string.
        index, n = 0, len(traversal)
        stack = []  # stack to hold (node, depth)
        
        while index < n:
            # First, determine the depth (number of dashes)
            depth = 0
            while index < n and traversal[index] == '-':
                depth += 1
                index += 1
                
            # Now, determine the node's value
            value = 0
            while index < n and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1
                
            # Create the new node
            node = TreeNode(value)
            
            # If the stack's size is greater than the current depth, pop until it fits
            while len(stack) > depth:
                stack.pop()
            
            # If there's a node in the stack, the new node is a child of that node.
            if stack:
                parent = stack[-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
                    
            # Push the current node onto the stack along with its depth
            stack.append(node)
        
        # The first element in the stack (or the bottom-most node) is the root.
        while len(stack) > 1:
            stack.pop()
        return stack[0]
