# URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # Use BFS iteratively using a queue since BFS returns level order nodes
        # O(n) time complexity to process each node
        # O(n) space complexity for output structure with n nodes
        if not root:
            return []
        levels = []
        level = 0
        queue = [root]
        while queue:
            # Keep track of level currently at by incrementing each while loop. Can do this since we know we've processed
            # each node in previous level by clearing out current queue nodes at current level first.
            # The length of the queue holds the length level since the number of child
            # nodes which are pushed to queue are the number of nodes to process by popping and appending more child nodes 
            # if necessary
            levels.append([])
            
            level_length = len(queue)
            
            for i in range(level_length):
                curr = queue.pop(0)
                levels[level].append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
            level += 1
        
        return levels

        # Recursive version of iterative version above
        if not root:
            return []
        levels = []

    
        def helper(node, level):
            if len(levels) == level:
                levels.append([])
                
            # Append current node val
            levels[level].append(node.val)
            
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
                
            
        helper(root, 0)
        return levels
    
        
