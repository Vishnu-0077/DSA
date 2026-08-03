class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def min(root):
    while root.left is not None:
        root = root.left
    return root.data
def max(root):
    while root.right is not None:
        root = root.right
    return root.data

if __name__ == '__main__':
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.left = Node(9)
    root.right.right = Node(14)

    print(min(root))
    print(max(root))
    