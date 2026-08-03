class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def min_bst(root):
    while root.left is not None:
        root = root.left
    return root.data

def max_bst(root):
    while root.right is not None:
        root = root.right
    return root.data

def count(root):
    if root is None:
        return 0
    return count(root.left) + count(root.right) + 1

def validate(root):
    if root is None:
        return True
    if root.left and max_bst(root.left) > root.data:
        return False
    if root.right and root.data > min_bst(root.right):
        return False
    return validate(root.left) and validate(root.right)

def biggest_bst(root):
    if root is None:
        return 0
    if validate(root):  # whole subtree is a BST
        return count(root)
    # otherwise check left and right subtrees
    return max(biggest_bst(root.left), biggest_bst(root.right))


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
root.left.left.right.right = Node(4)

print(biggest_bst(root))