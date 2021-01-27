# URL: https://leetcode.com/problems/merge-two-sorted-lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Simple iterative while loop to add in the value from each linked list depending on which one is lower
        # O(m + n) runtime complexity where m and n represent the different lengths of the linked lists
        # O(n) space complexity to store new merged linked list to return
        res = ListNode()
        
        curr_val_1 = None 
        curr_val_2 = None
        head = 0
        if l1 is None and l2 is None:
            return None
        
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
        
        res = ListNode()
        head = res
        
        while l1 is not None or l2 is not None:
            # Case where we need to check both cases
            if l1 is not None and l2 is not None:
                if l1.val <= l2.val:
                    res.val = l1.val
                    l1 = l1.next
                    res.next = ListNode()
                    res = res.next
                else:
                    res.val = l2.val
                    l2 = l2.next
                    res.next = ListNode()
                    res = res.next
            elif l1 is not None:
                while l1.next is not None:
                    res.val = l1.val
                    l1 = l1.next
                    res.next = ListNode()
                    res = res.next
                res.val = l1.val
                l1 = l1.next
            else:
                while l2.next is not None:
                    res.val = l2.val
                    l2 = l2.next
                    res.next = ListNode()
                    res = res.next
                res.val = l2.val
                l2 = l2.next
        
        return head
        
        
        # Simple solution of iterating through lists and then sorting them...
        # O(nlog(n)) runtime for sorting the resulting numbers
        # O(n) space complexity for storing numbers in array and storing new ListNodes
        if l1 == None and l2 == None:
            return None
        
        res = []
        
        if l1 is not None:
            while l1.next != None:
                res.append(l1.val)
                l1 = l1.next
            res.append(l1.val)
        
        if l2 is not None:

            while l2.next != None:
                res.append(l2.val)
                l2 = l2.next
            res.append(l2.val)

        # Recreate ListNode
        if len(res) == 0:
            return ListNode(val=None, next=None)
        elif len(res) == 1:
            return ListNode(val=res[0], next=None)
        else:
            res = sorted(res)
            result = ListNode(val=res[0], next=None)
            head = result
            for i in range(1, len(res)):
                result.next = ListNode(val=res[i], next=None)
                if i != len(res) - 1:
                    result = result.next
            return head
                
