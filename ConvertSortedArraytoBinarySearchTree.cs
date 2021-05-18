// URL: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
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
// Idea here is to recursively divide tree in to
// left and right sections. Since we know the array
// is sorted, we can append the middle of the left integers in the array
// as the left node and the middle of the right integers in the array
// as the right node recursively until low is greater than high, 
// which means a null node should be placed there.
// O(n) time complexity to iterate over every node where n is the number of nodes
// O(log(n)) time complexity for recursive stack for each call in balanced BST
public class Solution {
    public TreeNode SortedArrayToBST(int[] nums) {
        if (nums.Length == 0) {
            return null;
        }
        
        return Helper(nums, 0, nums.Length - 1);
    }
    
    public TreeNode Helper(int[] nums, int low, int high) {
        if (low > high) {
            return null;
        }
        
        int mid = (low + high) / 2;
        TreeNode node = new TreeNode(nums[mid]);
        node.left = Helper(nums, low, mid - 1);
        node.right = Helper(nums, mid + 1, high);
        
        return node;
    }
}
