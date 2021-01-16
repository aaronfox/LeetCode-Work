# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
# URL: https://leetcode.com/problems/merge-k-sorted-lists
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Runtime: priority queue inserts take O(log(n)) time with a while loop that lasts for every number value v
        # Runtime complexity is therefore O(v * log(n))
        # Space Complexity is O(n) for priority queue to hold all lists 
        # Would be easy to use a priority queue at the top with the lowest value prioritized
        pQueue = []
        # Each item in priority queue is stored as (val, index)
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(pQueue, (lists[i].val, i))
        
        mergedList = []
        mergedLinkedList = None
        root = None
        
        while len(pQueue) != 0:
            # Add from top of pQueue
            temp = heapq.heappop(pQueue)
            mergedList.append(temp[0])
            if mergedLinkedList is None:
                mergedLinkedList = ListNode(temp[0], None)
                root = mergedLinkedList
            else:
                mergedLinkedList.next = ListNode(temp[0], None)
                mergedLinkedList = mergedLinkedList.next
                
            # If object has next value
            if lists[temp[1]].next != None:
                lists[temp[1]] = lists[temp[1]].next
                heapq.heappush(pQueue, (lists[temp[1]].val, temp[1]))
        
        return root
                
