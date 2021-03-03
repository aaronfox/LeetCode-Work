# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# URL: https://leetcode.com/problems/symmetric-tree
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # O(n) runtime complexity where n is number of nodes
        # O(n) space complexity for recursive call on every node
        if not root.left and not root.right:
            return True
        return self.symmetricHelper(root.left, root.right)
    
        # Checking preorder vs postorder ordering only works for full trees, not unbalanced trees.
        # elif root.left and root.right:
        #     if self.getPreOrderTraversalIterative(root.left) == self.getPostOrderTraversalIterative(root.right):
        #         return True
        # return False
        # print(self.getPostOrderTraversalIterative(root))
        # print(self.getPreOrderTraversalIterative(root))

     
    def symmetricHelper(self, left, right):
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
        return self.symmetricHelper(left.left, right.right) and self.symmetricHelper(left.right, right.left)
        
    def getPreOrderTraversalIterative(self, node):
        stack = [node]
        res = []
        while stack:
            curr_node = stack.pop()
            res.append(curr_node.val)
            if curr_node.left:
                stack.append(curr_node.left)
            if curr_node.right:
                stack.append(curr_node.right)
        
        return res
    
    def getPostOrderTraversalIterative(self, node):
        queue = [node]
        res = []
        while queue:
            curr_node = queue.pop(0)
            res.append(curr_node.val)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        
        return res
