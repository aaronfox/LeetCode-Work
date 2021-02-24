"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# URL: https://leetcode.com/problems/n-ary-tree-preorder-traversal
# Recursive solution is trivial
# O(v) runtime complexity where v is the number of vertices
# O(n) space complexity where n is the number of nodes since each child needs a call
# Iterative solution needs a stack and to iterate over children backwards
# O(n) runtime complexity
# O(n) space complexity
class Solution:
    def __init__(self):
        self.res = []
        
    def preorder(self, root: 'Node') -> List[int]:
        # Iterative solution
        if root is None:
            return None
    
        res = []
        stack = []
        stack.append(root)
        
        while len(stack) > 0:
            root = stack.pop()
            res.append(root.val)
            for i in range(len(root.children) - 1, -1, -1):
                stack.append(root.children[i])
        return res
        # Recursive solution
    #     if root is None:
    #         return None
    #     self.res.append(root.val)
    #     self.recursive(root)
    #     return self.res
    # def recursive(self, root):
    #     if root is not None:
    #         for child in root.children:
    #             self.res.append(child.val)
    #             self.recursive(child)
    
    
        
