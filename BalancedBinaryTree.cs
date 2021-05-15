// URL: https://leetcode.com/problems/balanced-binary-tree/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
// Here, create a helper Depth function that calculates the max
// depth from each root. Then, use the Depth helper function
// in the IsBalanced function and recursively call IsBalanced
// ensuring that the difference between the two node depths
// is no more than 1.
public class Solution {
    public bool IsBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        
        int left = Depth(root.left);
        int right = Depth(root.right);

        return Math.Abs(left - right) <= 1 && IsBalanced(root.left) && IsBalanced(root.right);
     
    }
    
    public int Depth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        return Math.Max(Depth(root.left), Depth(root.right)) + 1;
    }
}