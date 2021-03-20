# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
# URL: https://leetcode.com/problems/merge-k-sorted-lists
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Merge lists with divide and conquer
        # Continually pair up K lists and merge each pair
        # O(nlog(k)) time complexity
        # O(1) space complexity
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        if len(lists) > 0:
            return lists[0]
        return None
    
        
    def mergeTwoLists(self, list1, list2):
        head = point = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                point.next = list1
                list1 = list1.next
            else:
                point.next = list2
                list2 = list1
                list1 = point.next.next
            point = point.next
        if not list1:
            point.next = list2
        else:
            point.next = list1
    
        return head.next
    
        
        
        
        
        
#         # Runtime: priority queue inserts take O(log(n)) time with a while loop that lasts for every number value v
#         # Runtime complexity is therefore O(v * log(n))
#         # Space Complexity is O(n) for priority queue to hold all lists 
#         # Would be easy to use a priority queue at the top with the lowest value prioritized
#         pQueue = []
#         # Each item in priority queue is stored as (val, index)
#         for i in range(len(lists)):
#             if lists[i] is not None:
#                 heapq.heappush(pQueue, (lists[i].val, i))
        
#         mergedList = []
#         mergedLinkedList = None
#         root = None
        
#         while len(pQueue) != 0:
#             # Add from top of pQueue
#             temp = heapq.heappop(pQueue)
#             mergedList.append(temp[0])
#             if mergedLinkedList is None:
#                 mergedLinkedList = ListNode(temp[0], None)
#                 root = mergedLinkedList
#             else:
#                 mergedLinkedList.next = ListNode(temp[0], None)
#                 mergedLinkedList = mergedLinkedList.next
                
#             # If object has next value
#             if lists[temp[1]].next != None:
#                 lists[temp[1]] = lists[temp[1]].next
#                 heapq.heappush(pQueue, (lists[temp[1]].val, temp[1]))
        
#         return root
                
