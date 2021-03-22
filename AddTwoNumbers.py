# URL: https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Here, just carry out basic grade school addition starting from least significant digit
        # at head of each linked list and keep iterating and adding a new node to answer
        # until the lists have no more nodes and until the carry bit is 0
        # O(n+m) time complexity where n and m are the lengths of the linked lists
        # O(n) space complexity to store output linked list
        carry = 0
        curr_node = ListNode(0)
        head = curr_node
        
        while l1 or l2 or carry != 0:
            curr_val = 0
            if l1:
                curr_val += l1.val
            if l2:
                curr_val += l2.val
                
            # Add carry bit
            curr_val += carry
            # Can get carry bit by dividing by 10 and making sure it's an int (flooring basically)
            carry = int(curr_val / 10)
            curr_node.val = curr_val % 10
            
            # Advance each node if needed
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
            if l1 or l2 or carry != 0:
                next_node = ListNode(0)
                curr_node.next = next_node
                curr_node = curr_node.next
            

            
        return head
    
#         l1_int = int(Solution.numToString(l1))
#         l2_int = int(Solution.numToString(l2))
#         answer_str = str(l1_int + l2_int)
#         print("answer_str == " + answer_str)
        
#         head = ListNode(answer_str[-1:])
#         curr_node = head
#         answer_str = answer_str[:-1]
#         while(answer_str != ""):
#             new_node = ListNode(answer_str[-1:])
#             curr_node.next = new_node
#             curr_node = new_node
#             # print(answer_str[-1:])
#             answer_str = answer_str[:-1]
#             # answer = ListNode()
#         return head
        

#     def numToString(list):
#         list_str = "";
#         while list != None:
#             list_str = str(list.val) + list_str;
#             list = list.next
#         return list_str
        

        
