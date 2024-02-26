class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { 
        val = x; 
    }
}

public class BinaryTree {

    public boolean isSameTree(TreeNode p, TreeNode q) {
        // Base case: If both nodes are null, they are the same
        if (p == null && q == null) {
            return true;
        }
        // If one of the nodes is null and the other is not, they are different
        if (p == null || q == null) {
            return false;
        }
        // If the values of the nodes are different, they are different trees
        if (p.val != q.val) {
            return false;
        }
        // Recursively check the left subtree and the right subtree
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }

    public static void main(String[] args) {
        // Create example binary trees
        TreeNode p = new TreeNode(1);
        p.left = new TreeNode(2);
        p.right = new TreeNode(3);

        TreeNode q = new TreeNode(1);
        q.left = new TreeNode(2);
        q.right = new TreeNode(3);

        // Create an instance of the SameBinaryTree class
        BinaryTree solution = new BinaryTree();

        // Check if the two trees are the same
        boolean result = solution.isSameTree(p, q);

        // Print the result
        if (result) {
            System.out.println("The two binary trees are the same.");
        } else {
            System.out.println("The two binary trees are not the same.");
        }
    }
}
