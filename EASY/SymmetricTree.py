''' Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false

 '''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True  # An empty tree is symmetric
        
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        if not t1 and not t2:
            return True  # Both are None, so symmetric
        if not t1 or not t2:
            return False  # One is None, the other is not
        
        # Check if values are the same and the subtrees are mirrors
        return (t1.val == t2.val and 
                self.isMirror(t1.left, t2.right) and 
                self.isMirror(t1.right, t2.left))

# Helper function to build a tree from a list (for testing)
def buildTree(values):
    if not values:
        return None
    
    nodes = [TreeNode(val) if val is not None else None for val in values]
    
    for i, node in enumerate(nodes):
        if node is not None:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(nodes):
                node.left = nodes[left_idx]
            if right_idx < len(nodes):
                node.right = nodes[right_idx]
    
    return nodes[0]  # Return root node

# Sample main function for testing
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Symmetric tree
    root = buildTree([1, 2, 2, 3, 4, 4, 3])
    print(solution.isSymmetric(root))  # Expected output: True

    # Test case 2: Non-symmetric tree
    root = buildTree([1, 2, 2, None, 3, None, 3])
    print(solution.isSymmetric(root))  # Expected output: False
