# URL: https://leetcode.com/problems/construct-string-from-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        # Recursive solution that checks if left exists
        # If it does, then add it with parens
        # If not and right exists, add empty parens
        # If right exists, then add it with parens
        # O(n) runtime where n is the number of nodes in the tree
        # O(n) space complexity for the n calls required in the recursive stack
        if t is None:
            return ""
        
        res = str(t.val)
        
        # If left exists
        if t.left:
            res += "(" + self.tree2str(t.left) + ")"
            
        # If left doesn't exist but right does
        if not t.left and t.right:
            res += "()"
            
        if t.right:
            res += "(" + self.tree2str(t.right) + ")"
        
        return res
    
        # self.visitNode(t)
        
    # def visitNode(self, node):
    #     printed = False
    #     if node.left is not None:
    #         print(str(node.val) + "(", end='')
    #         printed = True
    #         self.visitNode(node.left)
    #     if node.right is not None:
    #         if not printed:
    #             print(str(node.val) + "(", end='')
    #         self.visitNode(node.right)
    #     if node.left is None and node.right is None:
    #         print("(" + str(node.val) + "))", end='')
    #         # print("()", end='')
        
