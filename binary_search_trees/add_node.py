class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def add_node(root, add):
    cur = root
    while True:
        if add<cur.data:
            if cur.left is not None:
                cur = cur.left
            else:
                cur.left = Node(add)
                break
        else:
            if cur.right is not None:
                cur = cur.right
            else:
                cur.right = Node(add)
                break
    return root.data


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.left = Node(9)
root.right.right = Node(14)
print(add_node(root, 5))
        