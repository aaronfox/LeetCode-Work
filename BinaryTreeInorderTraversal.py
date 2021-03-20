# URL: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # Iterative solution. Use stack
        # O(n) time complexity to iterate over every node
        # O(n) space complexity for stack usage
        res = []
        stack = []
        curr = root
        while curr is not None or len(stack) > 0:
            # Keep going leftward until we reach None
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            # Then pop last leftward node from stack and append its value
            curr = stack.pop()
            res.append(curr.val)
            # Proceed to do the same thing but for its right node
            curr = curr.right
        
        return res
        
        # Recursive solution is trivial
        # O(n) as recursive function is T(n) = 2 * T(n/2) + 1
        # O(n) space complexity for recursive stack but average case of O(log(n))
        res = []
        self.helper(root, res)
        return res
    
        # Inorder is left, root, right order (increasing order of BST)
        if not root:
            return
        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)
        
        return self.res
        
    def helper(self, root, res):
        if root is None:
            return
        
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)
