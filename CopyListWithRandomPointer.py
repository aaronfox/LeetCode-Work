# URL: https://leetcode.com/problems/copy-list-with-random-pointer/

class Solution:
    """
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # O(n) time complexity to iterate over every node in old list
    # O(n) space complexity for storing already existing nodes in hashmap
    def __init__(self):
        self.visited_nodes = {}
        
    def getClonedNode(self, node):
        # Return resulting copied node or referenced node if it already is in hashmap
        res_node = None
        if node:
            if node in  self.visited_nodes:
                res_node =  self.visited_nodes[node]
            else:
                self.visited_nodes[node] = Node(node.val, None, None)
                res_node =  self.visited_nodes[node]

        return res_node
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        # Use a hashmap to keep track of node references already created
        visited_nodes = {}
        old_node = head
        new_node = Node(old_node.val, None, None)
        self.visited_nodes[old_node] = new_node
        
        # Iterate over old linked list until all nodes are cloned
        # Note: could abstract away the two if-if-else loops here into
        # a get_cloned_node method since they both are effectively doing the same thing
        while old_node:
            # Set new_node's random
            new_node.random = self.getClonedNode(old_node.random)
            
            # Set new_node's next
            new_node.next = self.getClonedNode(old_node.next)

            # Continue next step in iteration
            old_node = old_node.next
            new_node = new_node.next
            
        return  self.visited_nodes[head]
    
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         if not head:
#             return head
        
#         # Use a hashmap to keep track of node references already created
#         visited_nodes = {}
#         old_node = head
#         new_node = Node(old_node.val, None, None)
#         visited_nodes[old_node] = new_node
        
#         # Iterate over old linked list until all nodes are cloned
#         # Note: could abstract away the two if-if-else loops here into
#         # a get_cloned_node method since they both are effectively doing the same thing
#         while old_node:
#             # Set new_node's random
#             old_node_random = None
#             if old_node.random:
#                 if old_node.random in visited_nodes:
#                     old_node_random = visited_nodes[old_node.random]
#                 else:
#                     visited_nodes[old_node.random] = Node(old_node.random.val, None, None)
#                     old_node_random = visited_nodes[old_node.random]
            
#             new_node.random = old_node_random
            
#             # Set new_node's next
#             old_node_next = None
#             if old_node.next:
#                 if old_node.next in visited_nodes:
#                     old_node_next = visited_nodes[old_node.next]
#                 else:
#                     visited_nodes[old_node.next] = Node(old_node.next.val, None, None)
#                     old_node_next = visited_nodes[old_node.next]
                    
#             new_node.next = old_node_next
            
#             # Continue next step in iteration
#             old_node = old_node.next
#             new_node = new_node.next
            
#         return visited_nodes[head]
