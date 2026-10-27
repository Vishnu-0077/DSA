class Node:
    def __init__(self, url = None):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(url = homepage)
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.curr = self.head


    def visit(self, url: str) -> None:
        new_node = Node(url)
        cur_node = self.curr

        cur_node.next = new_node
        new_node.prev = cur_node

        new_node.next = self.tail
        self.tail.prev = new_node

        self.curr = new_node

    def back(self, steps: int) -> str:
        while steps!=0 and self.curr!=self.head:
            self.curr = self.curr.prev
            steps-=1

        return self.curr.url

    def forward(self, steps: int) -> str:
        while steps!=0 and self.curr!=self.tail.prev:
            self.curr = self.curr.next
            steps-=1
        
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)