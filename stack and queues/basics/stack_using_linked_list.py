class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,x):
        new_node = Node(x)  #it is adding the things in reverse, so have it soo like-- top -> 30 -> 20 -> 10
        new_node.next=self.head
        self.head = new_node
        self.size+=1

    def pop(self):
        if self.head is None:  #here it is following the same logic as linked list, top refers to head. wait let me change
            print("stack is empty")
            return
        x=self.head
        self.head=self.head.next
        self.size-=1
        return x.data
    
    def Top(self):
        return self.head.data
    
    def Size(self):
        return self.size
    
if __name__ == "__main__":
    s=Stack()
    s.push(6)
    s.push(3)
    s.push(6)
    print(f"the final size of the stack is {s.Size()},{s.Top()}")
    s.pop()
    print(f"after poping an element the size and the top value is {s.Size()},{s.Top()}")

        



        

