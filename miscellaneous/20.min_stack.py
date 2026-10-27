class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.topi = -1
    def push(self, value: int) -> None:
        self.stack.append(value)
        self.topi+=1
        if self.min_stack and value<=self.min_stack[-1]:
            self.min_stack.append(value)
        if not self.min_stack:
            self.min_stack.append(value)

    def pop(self) -> None:
        if self.min_stack and self.stack[self.topi]==self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
        self.topi-=1

    def top(self) -> int:
        return self.stack[self.topi]

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()