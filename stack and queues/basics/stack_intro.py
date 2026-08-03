class Stack:
    def __init__(self):
        self.top=-1
        self.size=1000
        self.arr=[0]*self.size

    def push(self,x):
        self.top+=1
        self.arr[self.top]=x
    
    def pop(self):
        x=self.arr[self.top]
        self.top-=1
        return x
    
    def Top(self):
        return self.arr[self.top]
    
    def Size(self):
        return self.top+1
    
if __name__ == '__main__':
    s=Stack()
    s.push(6)
    s.push(3)
    s.push(6)
    print(f"the final size of the stack is {s.Size()},{s.Top()}")
    s.pop()
    print(f"after poping an element the size and the top value is {s.Size()},{s.Top()}")
