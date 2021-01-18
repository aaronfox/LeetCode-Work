# URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # A pretty sloppy O(n) time complexity approach with a lot of ifs for edge cases
        # O(n) space complexity for storing copies of linked list
        # TODO: do this in one pass
        head_copy = head
        head_copy_copy = head_copy
        before = None
        # Get length of list
        count = 1
        while head.next is not None:
            count += 1
            head = head.next
            
        if count == 1:
            return None
        
        if count == 2:
            if n == 1:
                head_copy.next = None
                return head_copy
            
        if n == count:
                head_copy = head_copy.next
                return head_copy
            
        for i in range(count):
            if i == count - n - 1:
                before = head_copy_copy
                head_copy_copy = head_copy_copy.next
                break
            head_copy_copy = head_copy_copy.next
        
        before.next = head_copy_copy.next
        
        return head_copy
        
