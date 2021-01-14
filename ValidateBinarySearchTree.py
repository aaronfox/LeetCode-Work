# URL: https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Recursive Solution has an O(n) time complexity since each node is visited once
        # O(n) space complexity since there is a call for each node
        def validate(root, low, high):
            if root == None:
                print("None")
                return True

            if root.val <= low or root.val >= high:
                return False
            
            return validate(root.left, low, root.val) and validate(root.right, root.val, high)
        
        return validate(root, low = -math.inf, high = math.inf)
