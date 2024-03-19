package Week2;

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class IsSameTree {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // If both nodes are null, they are the same
        if (p == null && q == null)
            return true;
        // If one of the nodes is null and the other isn't, they are not the same
        if (p == null || q == null)
            return false;
        // If the values of the nodes are different, they are not the same
        if (p.val != q.val)
            return false;
        // Recursively check if the left and right subtrees are the same
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }

    public static void main(String[] args) {
        IsSameTree solution = new IsSameTree();

        // Example usage
        TreeNode p = new TreeNode(1);
        p.left = new TreeNode(2);
        p.right = new TreeNode(3);

        TreeNode q = new TreeNode(1);
        q.left = new TreeNode(2);
        q.right = new TreeNode(3);

        System.out.println(solution.isSameTree(p, q)); // Output: true
    }
}
