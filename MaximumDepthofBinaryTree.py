# URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Simple Recursive Solution
        # O(n) time complexity since every node is visited once
        # O(n) space complexity since every node has its own recursive call
        if root is None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        if left > right:
            return left + 1
        else:
            return right + 1
        
        
