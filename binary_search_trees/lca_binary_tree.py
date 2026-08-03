#return the latest common ancestors
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def lca(root, p ,q):
    while root:
        if p<root.data  and q<root.data:
            root = root.left
        elif p>root.data  and q>root.data:
            root = root.right
        else:
            return root.data
    else:
        return None

root = Node(9)
root.left = Node(5)
root.right = Node(11)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(10)
root.right.right = Node(13)
root.left.right.left = Node(6)
root.left.right.right = Node(8)
root.left.left.left = Node(1)
root.left.left.right = Node(3)

print(lca(root,4,6))