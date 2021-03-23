# URL: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # This solution uses constant space since no extra data structures are used
        # O(n) time complexity where n is the numberf of nodes
        # O(1) space complexity since no extra data structures are used here
        if not root:
            return None
        
        # Start wth root node and have leftmost traverse each level by going left continually
        # Can do this since we know tree is perfect
        leftmost = root
        
        while leftmost.left:
            head = leftmost
            
            while head:
                # Connection between two nodes with the same parents
                head.left.next = head.right
        
                # Connection between two non-common parents
                if head.next:
                    head.right.next = head.next.left
                
                # Proceed to next right node on same level
                head = head.next
                
            leftmost = leftmost.left
            
        return root
        
        
        
        # BFS Traversal. Get each level in order using BFS
        # and then iterate over each level setting its next pointer
        # appropriately
        # O(n) time complexity to process each node once
        # O(n) space complexity for storing each node in levels queue
        if not root:
            return None
        
        queue = [root]
        levels = []
        level = 0
        
        while len(queue) > 0:
            levels.append([])
            
            for i in range(len(queue)):
                curr = queue.pop(0)
                levels[level].append(curr)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
                    
            # Now have each node in current level in levels       
            for i in range(len(levels[level])):
                if i == len(levels[level]) - 1:
                    levels[level][i].next = None
                else:
                    levels[level][i].next = levels[level][i + 1]
                    
            level += 1
            
        return root
                        
