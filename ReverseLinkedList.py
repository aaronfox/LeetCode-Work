# URL: https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # In the iterative approach, we just need to keep track of previous node and current node
        # At every iteration, store current node in temp variable, then set next node of current node to previous node
        # Set previous node to current node and set next node to be the temp node again.
        # O(n) runtime complexity where n is the list's length
        # O(1) space complexity
        if not head or not head.next:
            return head
        curr = head
        prev = None
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        
        return prev
    
        # Recursive solution
        # O(n) time complexity
        # O(n) space complexity for recursive stack
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
