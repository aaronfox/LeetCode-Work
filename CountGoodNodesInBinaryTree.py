# URL: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursively update max value as we go down tree in depth-first manner
    # If current node's value is greater than current max, add it to count
    # Return total count
    # O(n) time complexity for searching through each node (n represents each node)
    # O(h) space complexity where h represents the height of the tree and therefore length 
    # of recursive stack
    def goodNodes(self, root: TreeNode) -> int:
        # Use DFS and keep track of maximum number of nodes
        return self.dfs(root, root.val)
        
    def dfs(self, root, maximum):
        if root is None:
            return 0;
        
        res = 0
        if root.val >= maximum:
            res += 1
            
        res += self.dfs(root.left, max(maximum, root.val))
        res += self.dfs(root.right, max(maximum, root.val))
        
        return res
