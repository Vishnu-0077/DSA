# Creating a Node and a Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.reference = None

class LinkedList:
    def __init__(self):
        self.head = None

# Example usage
node1 = Node(7)
print(node1.data)
print(node1.reference)  
