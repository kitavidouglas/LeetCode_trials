package Week3;

public class TreeNode_Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return false;
        }
        
        if (root.left == null && root.right == null) { // Check if it's a leaf node
            return root.val == targetSum;
        }
        
        // Recursively search for the target sum in the left and right subtrees
        return hasPathSum(root.left, targetSum - root.val) || hasPathSum(root.right, targetSum - root.val);
    }

    public static void main(String[] args) {
        // Example usage
        // Construct the binary tree [1,2,3]
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);

        int targetSum = 5;
        TreeNode_Solution solution = new TreeNode_Solution();
        System.out.println(solution.hasPathSum(root, targetSum)); // Output: false

        // Example usage with an empty tree
        System.out.println(solution.hasPathSum(null, 0)); // Output: false
    }
}

