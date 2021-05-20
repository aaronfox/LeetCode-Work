// URL: https://leetcode.com/problems/insertion-sort-list/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
// Use dummy node which is the node right before first node and has
// a next pointer to the first node of the list based on prev.next = curr.
// Then use current node pointer to represent node to be inserted, previous
// node pointer for going along the nodes in the manner of insertion sort
// and a next node which is used as a temp variable when swapping two nodes
// O(n^2) runtime complexity to iterate over all nodes
// O(1) space complexity 
public class Solution {
    public ListNode InsertionSortList(ListNode head) {
        if (head == null) {
            return head;
        }
        
        ListNode dummy = new ListNode(); // starter of the list
        ListNode curr = head; // curr is the node to be inserted
        ListNode prev = dummy; // node should be inserted between prev and prev.next
        ListNode next = null; // the next node that will be inserted
        
        while (curr != null) {
            // Find place to insert next node
            while (prev.next != null && prev.next.val < curr.val) {
                prev = prev.next;
            }
            
            // Insert between prev and prev.next
            next = curr.next; 
            curr.next = prev.next;
            prev.next = curr;
            
            // Reset prev to original dummy node at beginning of list
            prev = dummy;
            
            // Advance curr node to next
            curr = next;
            
        }
        
        return dummy.next;
    }
}
