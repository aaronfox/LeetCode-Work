# URL: https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Two pointer implementation
        # Have a fast pointer that goes 2 steps and a slow pointer that goes 1 step
        # If the fast pointer meets the slow pointer, return True (has a cycle).
        # If fast pointer meets None (the end) then return False (no cycle detected).
        # O(n) time complexity
        # O(1) space complexity
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
        # hashmap implementation
        # O(n) time complexity
        # O(n) space complexity
        hashmap = {}
        while head:
            if head in hashmap:
                return True
            hashmap[head] = True
            head = head.next
        
        return False
