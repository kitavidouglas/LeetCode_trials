package Week5;


public class TreeNode_MaxDepth {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        // Recursively calculate the depth of the left and right subtrees
        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);
        
        // Return the maximum depth among the left and right subtrees, plus 1 (for the current node)
        return Math.max(leftDepth, rightDepth) + 1;
    }

    public static void main(String[] args) {
        // Example usage
        // Construct the binary tree [3,9,20,null,null,15,7]
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        TreeNode_MaxDepth maxDepthCalculator = new TreeNode_MaxDepth();
        System.out.println(maxDepthCalculator.maxDepth(root)); // Output: 3
    }
}