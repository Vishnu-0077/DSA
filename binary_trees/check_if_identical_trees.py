class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def ident(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return root1.data == root2.data and ident(root1.left,root2.left) and ident(root1.right,root2.right)

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)

root2 = Node(1)
root2.left = Node(3)
root2.right = Node(2)
root2.left.left = Node(7)
root2.left.right = Node(6)
root2.right.left = Node(5)
root2.right.right = Node(4)

print(ident(root1,root2))

#check only if 2 trees are exactly identical, summa ah lite