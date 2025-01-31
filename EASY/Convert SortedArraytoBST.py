''' Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs

'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None  # Base case: empty array

        mid = len(nums) // 2  # Middle element
        root = TreeNode(nums[mid])  # Create root node

        # Recursively build left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])  # Left half
        root.right = self.sortedArrayToBST(nums[mid+1:])  # Right half

        return root

# Helper function to print tree in level-order for verification
def levelOrderTraversal(root):
    if not root:
        return []
    
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Trim trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
    
    return result

# Sample main function for testing
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [-10, -3, 0, 5, 9]
    root1 = solution.sortedArrayToBST(nums1)
    print(levelOrderTraversal(root1))  # Expected: [0, -3, 9, -10, None, 5]

    # Test case 2
    nums2 = [1, 3]
    root2 = solution.sortedArrayToBST(nums2)
    print(levelOrderTraversal(root2))  # Expected: [3, 1] or [1, None, 3]
