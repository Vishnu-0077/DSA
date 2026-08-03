class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def number_of_node(root):
    if root is None:
        return 0
    return 1 + number_of_node(root.left) + number_of_node(root.right)

def kth_largest_number(root, k):
    count_right = number_of_node(root.right)
    count_node = number_of_node(root)

    # If k-th largest is the root
    if k == count_right + 1:
        return root.data
    # If it's in the right subtree
    elif k <= count_right:
        return kth_largest_number(root.right, k)
    # If it's in the left subtree
    elif k <= count_node:
        return kth_largest_number(root.left, k - count_right - 1)
    else:
        return None  # k is larger than total nodes

# Example tree
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

print(kth_largest_number(root, 3))  
