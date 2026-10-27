class Node:
    def __init__(self, key=0, value=0):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after_head(self, Node):
        Node.next = self.head.next
        self.head.next = Node

        Node.next.prev = Node
        Node.prev = self.head
    
    def remove(self, Node):
        next_node = Node.next
        prev_node = Node.prev

        prev_node.next = Node.next
        next_node.prev = prev_node

        Node.next = None
        Node.prev = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert_after_head(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.remove(node)
            self.insert_after_head(node)
        
        else:
            if self.capacity==len(self.cache):
                rem_node = self.tail.prev
                self.remove(rem_node)
                del self.cache[rem_node.key]
            
            node = Node(key = key, value = value)
            self.cache[key] = node
            self.insert_after_head(node)
        
