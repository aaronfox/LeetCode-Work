# URL: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
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
    # O(n) time complexity to process each node once
    # O(1) space complexity since no additional data structures are used
    def __init__(self):
        self.prev = None
        self.leftMost = None
        
    def processChild(self, node):
        if node:
            if self.prev:
                self.prev.next = node
            else:
                self.leftMost = node

            self.prev = node
        
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        self.leftMost = root

        curr = self.leftMost

        while self.leftMost:
            self.prev = None
            curr = self.leftMost

            self.leftMost = None

            while curr:
                self.processChild(curr.left)
                self.processChild(curr.right)

                curr = curr.next

        return root
