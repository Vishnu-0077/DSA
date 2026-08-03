class Node:
    def __init__(self, data):
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

def is_bst_for_immediate_children(root):
    if root is None:
        return True
    root_left, root_right = root.left, root.right
    if root.left and root_left.data>root.data:
        return False
    if root.right and root_right.data<root.data:
        return False
    return is_bst_for_immediate_children(root.left) and is_bst_for_immediate_children(root.right)

def bst_for_whole(root):
    if root is None:
        return True
    if root.left and max_bst(root.left)>root.data:
        return False
    if root.right and root.data>min_bst(root.right):
        return False
    return bst_for_whole(root.left) and bst_for_whole(root.right)


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

print(is_bst_for_immediate_children(root))
print(bst_for_whole(root))
    