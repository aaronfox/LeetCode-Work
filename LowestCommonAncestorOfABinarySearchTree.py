# URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Algorithm: 
        # 1. Start traversing tree from root
        # 2. If both p and q are in right subtree, continue search with right subtree starting at step 1
        # 3. If both p and 1 are in left subtree, continue search with subtree starting at step 1
        # 4. If both step 2 and step 3 aren't true, we found the common node for p and 1 and we can
        #    return this node
        # O(n) time complexity to traverse all noeds in worst case of BST
        # O(n) space complexity to possible recurse over all nodes
        # NOTE: could also do this iteratively since and we wouldn't have to backtrack
        #       and just set the node value to either its left or right child every time
        
        parent_val = root.val
        
        p_val = p.val
        
        q_val = q.val
        
        # If both values are greater than parent val, traverse right
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If both valuesa re less than the parent val, traverse left
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        # Otherwise, we found the split point where one node is greater than current node
        # and one node is less than the current node so this is the LCA node
        else:
            return root
