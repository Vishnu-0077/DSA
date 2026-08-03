class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def number_of_node(root):
    if root is None:
        return 0
    return 1 + number_of_node(root.left) + number_of_node(root.right)


def kth_smallest_number(root,k):
    count_left = number_of_node(root.left)
    count_node = number_of_node(root)

    if k==count_left+1:
        return root.data
    elif k<=count_left:
        return kth_smallest_number(root.left,k)
    elif k<=count_node:
        return kth_smallest_number(root.right,k-count_left-1)
    else:
        return root.data

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
print(kth_smallest_number(root,10))