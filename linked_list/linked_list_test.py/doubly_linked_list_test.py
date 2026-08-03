class Node():
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class doubly_linked_list():
    def __init__(self):
        self.head = None

    def forward_traversal(self):
        if self.head is None:
            print("Doubly linked list is empty")
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" ")
                a = a.next
    
    def backward_traversal(self):
        if self.head is None:
            print("Doubly linked list is empty")
        else:
            a = self.head
            while a.next is not None:
                a = a.next   #here we can go to the last node, without using tail, we go to the last node, then we are moving down from there using the while loop
            while a is not None:
                print(a.data, end=" ")
                a = a.prev

    def insert_at_beginning(self, data):
        new_node = Node(data)
        a= self.head
        new_node.next =a
        a.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node= Node(data)
        a=self.head
        while a.next is not None:
            a = a.next
        a.next = new_node
        new_node.prev = a

    def delete_at_beginning(self):
        a = self.head
        self.head = a.next
        a.next=None
        self.head.prev = None

    def delete_at_end(self):
        a=self.head
        while a.next is not None:
            a=a.next
        a.prev.next=None
        a.prev = None

    def insert_specfied_node(self,data,position):
        new_node=Node(data)
        a=self.head
        f=self.head.next
        for i in range(1,position-1):
            a=a.next
            f=f.next
        a.next= new_node
        new_node.prev = a
        new_node.next = f
        f.prev = new_node
    
    def delete_at_specific_position(self, position):
        a = self.head
        f = self.head.next
        for i in range(1, position - 1):
            a = a.next
            f = f.next
        a.next = f.next
        f.next.prev = a
        f.next = None
        f.prev = None
        


n1= Node(10)
n2= Node(20)
n3= Node(30)
n4= Node(40)

n1.next = n2
n2.next = n3
n3.next = n4
n2.prev = n1
n3.prev = n2
n4.prev = n3

dll= doubly_linked_list()
dll.head=n1
print(dll.insert_at_beginning(5))  # Insert at beginning
print(dll.insert_at_end(50))  # Insert at end
print(dll.delete_at_beginning())  # Delete at beginning
print(dll.delete_at_end())  # Delete at end
print(dll.insert_specfied_node(25, 3))  # Insert at specified position
print(dll.delete_at_specific_position(2))  # Delete at specific position
print(dll.forward_traversal())  # Output: 10 20 30 40
print(dll.backward_traversal())  # Output: 40 30 20 10
