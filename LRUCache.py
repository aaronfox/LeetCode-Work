# URL: https://leetcode.com/problems/lru-cache/
class DoublyLinkedListNode:
    def __init__(self):
        self.key = None
        self.value = None
        self.prev = None
        self.next = None

class LRUCache:
    # Can use a doubly linked list to keep track of order here
    # With the doubly linked list, we can use constant removes (with a reference)
    # and constant inserts to keep track of order efficiently. A DLL is useful
    # as it a value can be removed without worrying about other references
    # The hashmap can be used for constant checking of if a value is already in DLL
    # The hashmap stores the integer as its key and its Node reference as the values
    # O(1) runtime complexity since all hashmap and DLL ops take O(1) time
    # O(n) space complexity where n is the capacity for storing nodes in DLL and in hashmap

    def add_node(self, node):
        # Add node to be right after pseudohead to follow LRU protocol
        # e.g. if DLL is 1 - 2 - 3 with 1 being head and 3 being tail 
        #      and need to add 4, put 4 at 1 - 4 - 2 - 3
        # This is because head node is a pseudo head to mark a boundary
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
        
    def remove_node(self, node):
        # Remove node from DLL
        prev = node.prev
        new = node.next
        
        prev.next = new
        new.prev = prev
        
    def move_to_head(self, node):
        # Place node to be in front of pseudo head using two constant methods above
        self.remove_node(node)
        self.add_node(node)
        
    def pop_tail(self):
        # Remove tail node
        res = self.tail.prev
        self.remove_node(res)
        return res
        
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = DoublyLinkedListNode()
        self.tail = DoublyLinkedListNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache.get(key)
        
        # Move access node to head to follow LRU protocol
        self.move_to_head(node)
        
        return node.value
        

    def put(self, key: int, value: int) -> None:
        # Can either update existing value or create new value
        # If updating value also move it to head since it becomes LRU node
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
            return
        
        node = DoublyLinkedListNode()
        node.key = key
        node.value = value
        self.cache[key] = node
        self.add_node(node)

        if len(self.cache) > self.capacity:
            # Over capacity so must remove least-recently used node
            tail = self.pop_tail()
            del self.cache[tail.key]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
