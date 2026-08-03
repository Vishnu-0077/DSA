# TRAVERSAL IN LINKED LIST

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print("Singly linked list is empty")
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" ")
                a = a.next
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = new_node
    
    def insert_specified_node(self, data,position):
        new_node = Node(data)
        a=self.head
        for i in range(1,position-1):
            a = a.next
        new_node.next = a.next
        a.next= new_node

    def deletion_at_begining(self):
        a=self.head
        self.head = a.next
        a.next = None   

    def deletion_at_end(self):
        p=self.head
        a=self.head.next
        while a.next is not None:
            a=a.next
            p=p.next
        p.next = None

    def delete_at_specific_position(self,position):
        p=self.head
        a=self.head.next
        for i in range(1,position-1):
            a=a.next
            p=p.next
        p.next = a.next
        a.next = None

    def search_an_element(self,element):
        a=self.head
        while a is not None:
            if a.data==element: #here have to put that a.data==element. i dont know why
                return True
            a=a.next
        return False

#common practice, we initaite a temporary self.head in every def function that we make

# Creating nodes
n1 = Node(5)
n2 = Node(10)
n3 = Node(15)
n4 = Node(20)

# Linking nodes
n1.next = n2
n2.next = n3
n3.next = n4

# Creating singly linked list and assigning head
sll = SLL()
sll.head = n1

# inserting at first and transversing the list
sll.insert_at_beginning(3)
sll.insert_at_end(25)
sll.insert_specified_node(12, 3)
sll.deletion_at_begining()
sll.deletion_at_end()
sll.delete_at_specific_position(2)
print(sll.search_an_element(15))
sll.traversal()