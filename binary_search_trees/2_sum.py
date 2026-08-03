class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def sum_pair(root, target):
    if root is None:
        return False
    if root.left and root.data + root.left.data >= target:
        return True
    if root.right and root.data + root.right.data >= target:
        return True
    return sum_pair(root.left, target) or sum_pair(root.right, target)


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

print(sum_pair(root,23))