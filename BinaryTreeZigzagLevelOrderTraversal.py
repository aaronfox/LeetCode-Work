# URL: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # Use level order BFS with a queue keeping track of direction
        # Use deque-like object to append to end of array when going from right to left for 
        # FIFO queue behavior
        # and prepend to beginning of array when going from left to right
        # for FILO stack behavior
        # O(n) runtime complexity where n is the number of nodes in each tree
        # since inserting to end/beginning of a deque takes O(1) time
        # O(n) space complexity for storing each node in the queue and final output array
        if not root:
            return []
        
        levels = []
        curr_level = []
        # Use None delimiter to distinguish each level
        deque = [root, None]
        direction = 'left'
        
        while len(deque) > 0:
            curr_node = deque.pop(0)
            
            if curr_node:
                # Going right to left
                if direction == 'left':
                    # Append in FIFO queue order
                    curr_level.append(curr_node.val)
                else:
                    # Prepend for FILO stack order
                    curr_level.insert(0, curr_node.val)
                    
                if curr_node.left:
                    deque.append(curr_node.left)
                if curr_node.right:
                    deque.append(curr_node.right)
            else:
                # Current level is finished
                levels.append(curr_level)
                
                # Mark end of level with None delimiter
                # if there are still items child nodes left to process
                if len(deque) > 0:
                    deque.append(None)
                
                # Prep next level
                curr_level = []
                if direction == 'left':
                    direction = 'right'
                else:
                    direction = 'left'
                    
        return levels
