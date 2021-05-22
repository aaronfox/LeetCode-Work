// URL: https://leetcode.com/problems/min-stack/
public class MinStack {

    private Node head;
    /** initialize your data structure here. */
    public MinStack() {
       
    }
    
    public void Push(int val) {
        if (head == null)
        {
            head = new Node(val, val);
        }
        else 
        {
            // This is the key here: each node stores the minimum value at this 
            // node and below it. Above nodes that are inserted are not relevant
            // to this min stack.
            head = new Node(val, Math.Min(val, head.min), head);
        }
    }
    
    public void Pop() {
        head = head.next;
    }
    
    public int Top() {
        return head.val;
    }
    
    public int GetMin() {
        return head.min;
    }
    
        public class Node {
            public int val;
            public int min;
            public Node next;

            public Node(int val, int min) {
                this.val = val;
                this.min = min;
                this.next = null;
            }

            public Node(int val, int min, Node next) {
                this.val = val;
                this.min = min;
                this.next = next;
            }
        }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(val);
 * obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */
