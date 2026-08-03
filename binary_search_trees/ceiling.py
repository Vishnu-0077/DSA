#ceiling means return the lowest number that is just greater than the given value

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def ceiling(root, given):
    ans = -1
    while root is not None:
        if given>root.data:
            root = root.right
        else:
            ans = root.data
            root = root.left
    return ans

# Construct the tree from the image
root = Node(10)

# Left Subtree
root.left = Node(5)
root.left.left = Node(3)
root.left.right = Node(6)
root.left.left.left = Node(2)
root.left.left.right = Node(4)
root.left.right.right = Node(9)

# Right Subtree
root.right = Node(13)
root.right.left = Node(11)
root.right.right = Node(14)

print(ceiling(root,8))
