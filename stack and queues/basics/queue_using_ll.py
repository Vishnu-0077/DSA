class Node:
 def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size=0
        self.maxSize = 16

    def push(self,x): #here it is adding element in the rear, even iam having some confision here, what the hell is going onnn
        if self.front is None: #usually the near element in the queues should be added in the front
            self.front = Node(x)
            self.rear = self.front
        elif self.size == self.maxSize:
            print("queue is full")
        else:
            new_element = Node(x)
            self.rear.next = new_element
            self.rear = new_element
        self.size+=1

    def pop(self):
        if self.front is None:
            print("queue is empty")
        else:
            x=self.front #but popping from back
            self.front=self.front.next
            self.size-=1
            return x.data
        
    def top(self):
        if self.front is None:
            print("queue is empty")
        else:
            return self.rear.data

    def Size(self):
        return self.size
    
if __name__ == '__main__':
    q=Queue()
    q.push(6)
    q.push(3)
    q.push(6)
    print(f"the final size of the queue is {q.Size()},{q.top()}")
    q.pop()
    print(f"after poping an element the size and the top value is {q.Size()},{q.top()}")