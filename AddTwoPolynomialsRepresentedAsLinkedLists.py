# URL: https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/
# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        # Iterate through nodes keeping respect to rules of coefficients and powers
        # O(n + m) time complexity where n and m represent the lengths of each linked list
        # O(n) space complexity for storing output linked list
        head = None
        curr_node = None
        while poly1 or poly2:
            if poly1 and poly2:
                if poly1.power > poly2.power:
                    node_to_add = PolyNode(poly1.coefficient, poly1.power)
                    poly1 = poly1.next
                elif poly2.power > poly1.power:
                    node_to_add = PolyNode(poly2.coefficient, poly2.power)
                    poly2 = poly2.next
                else:
                    # Edge case wher sum of coefficients is 0
                    if poly1.coefficient + poly2.coefficient != 0:
                        node_to_add = PolyNode(poly1.coefficient + poly2.coefficient, poly1.power)
                    else:
                        node_to_add = None
                    poly1 = poly1.next
                    poly2 = poly2.next
            elif poly1:
                node_to_add = PolyNode(poly1.coefficient, poly1.power)
                poly1 = poly1.next
            elif poly2:
                node_to_add = PolyNode(poly2.coefficient, poly2.power)
                poly2 = poly2.next
            
            if not head and node_to_add:
                head = node_to_add
                curr_node = head
            elif node_to_add:
                curr_node.next = node_to_add
                curr_node = curr_node.next
            
                
        return head
    
