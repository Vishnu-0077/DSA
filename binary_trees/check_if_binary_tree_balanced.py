class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def height_of_binary_tree_stack_method(root):
    stack = []
    stack.append(root)
    height = 0
    while stack:
        for i in range(len(stack)):
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        height+=1
    return height

def check_if_balanced_subtree(root):
    node_left  = root.left
    node_right = root.right

    height_left=height_of_binary_tree_stack_method(node_left)
    height_right=height_of_binary_tree_stack_method(node_right)

    if abs(height_right - height_left) > 1:
        return False
    return check_if_balanced_subtree(node_left) and check_if_balanced_subtree(node_right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(check_if_balanced_subtree(root))

