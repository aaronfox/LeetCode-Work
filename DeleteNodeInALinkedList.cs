// URL: https://leetcode.com/problems/delete-node-in-a-linked-list/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
// This is a bit of a trick question. Since there 
// is no head given, we can only assign the value of the node to be the next
// node's values. This isn't ideal, of course. A better way to phrase this question
// would be ModifyNode instead of DeleteNode.
// O(1) time complexity
// O(1) space complexity
public class Solution {
    public void DeleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
