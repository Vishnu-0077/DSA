class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self,x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        
    def pop(self):
        x=self.stack[-1]
        self.stack.pop()
        if self.min_stack[-1]==x:
            self.min_stack.pop()
        return x
    
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.min_stack[-1]

if __name__ == "__main__":
    s = MinStack()
    s.push(5)
    s.push(3)
    s.push(7)
    print(s.getMin())  # Output: 3
    s.pop()
    print(s.getMin())  # Output: 3
    s.pop()
    print(s.getMin())  # Output: 5
