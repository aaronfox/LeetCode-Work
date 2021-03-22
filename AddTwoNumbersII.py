# URL: https://leetcode.com/problems/add-two-numbers-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Here we
        # 1. Get length of both lists for later parsing of linked lists
        # 2. Sum up each list into new linked list ignoring carry (e.g. 10 can be in an element)
        #    This results in a reverse linked list
        # 3. Using reverse linked list, go through each number including carry this time, prepending
        #    each value to new linked list
        #    If there is a carry at the end of this, add it to a new node at beginning
        # O(n + m) time where n is length of first length list and m is len(l2)
        # O(n) space complexity for storing output linked list
        # Find length of both lists to aid in parsing lists
        length_l1 = 0
        length_l2 = 0
        curr_l1 = l1
        curr_l2 = l2
        
        while curr_l1:
            length_l1 += 1
            curr_l1 = curr_l1.next
            
        while curr_l2:
            length_l2 += 1
            curr_l2 = curr_l2.next

        
        # Now parse lists and build reversed list so that we can easily
        # run through the lists next and correct the carries
        # by summing elements and ignoring carries (for now)
        curr_l1 = l1
        curr_l2 = l2
        head = None
        while length_l1 > 0 and length_l2 > 0:
            curr_val = 0
            # Keep track of lengths of each linked list
            # and if one list is larger than the other then
            # only add value of larger linked list
            # Both if loops will go through if they are at same length
            if length_l1 >= length_l2:
                curr_val += curr_l1.val
                curr_l1 = curr_l1.next
                length_l1 -= 1
            if length_l1 < length_l2:
                curr_val += curr_l2.val
                curr_l2 = curr_l2.next
                length_l2 -= 1
            
            curr_node = ListNode(curr_val)
            curr_node.next = head
            head = curr_node
            
        # Now that linked list is reversed, correct the carries
        curr_node = head
        head = None
        carry = 0
        while curr_node:
            total_val = curr_node.val + carry
            curr_val = total_val % 10
            carry = int(total_val / 10)
            
            # Prepend resulting node to resulting linked list
            # And make new node the head
            this_node = ListNode(curr_val)
            this_node.next = head
            head = this_node
            
            curr_node = curr_node.next
            
        # Check if we need to add the last carry
        if carry > 0:
            this_node = ListNode(carry)
            this_node.next = head
            head = this_node
            
        return head
        
