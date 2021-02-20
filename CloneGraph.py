"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# URL: https://leetcode.com/problems/clone-graph
class Solution:
    def __init__(self):
        self.map = {}
        
    # Use depth first search here to iteratively add neighbors
    def cloneGraph(self, node: 'Node') -> 'Node':
        # O(V + E) time complexity where V is the number of vertices and E the number of edges
        # O(V) space complexity
        if node == None:
            return None
        if node.val in self.map:
            return self.map[node.val]
        
        clone = Node(node.val)
        self.map[node.val] = clone
        for neighbor in node.neighbors:
            clone.neighbors.append(self.cloneGraph(neighbor))
        return clone
