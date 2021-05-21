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
// URL: https://leetcode.com/problems/minimum-depth-of-binary-tree/
public class Solution {
    public int MinDepth(TreeNode root) {
        // DFS approach
        // This approach isn't optimal if, say, the left subtree
        // had 5,000 nodes and the right subtree had 2 nodes because
        // this approach would cover the left 5,000 nodes first as
        // opposed to a BFS approach
        // Key approach here is that if a node has one child
        // then we must evaluate that node via Math.Max...
        // If two children, return min depth of both sides
        // via Math.Min...
        // O(n) runtime complexity to iterate over all possible nodes 
        // (not optimal using dfs. should use bfs to improve upon this)
        // O(n) space complexity to recursively iterate over all nodes
        if (root == null) {
            return 0;
        }
        int left = MinDepth(root.left);
        int right = MinDepth(root.right);
        if (left == 0 || right == 0) {
            return Math.Max(left, right) + 1;
        } else {
            return Math.Min(left, right) + 1;
        }
        
    }
}
