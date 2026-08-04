class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def left_view(root): #actually level order traversal only
    stack = []
    stack.append(root)
    hor = []
    while stack:
        for i in range(len(stack)):
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if i == 0: #we are just adding the first element of the level order traversal. so we add only the first element in the stack
                hor.append(node.data)
    return hor

def right_view(root):
    stack = []
    stack.append(root)
    hor = []
    while stack:
        for i in range(len(stack)):
            node = stack.pop(0)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if i == 0: #we are just adding the first element of the level order traversal. so we add only the first element in the stack
                hor.append(node.data)
    return hor

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.left = Node(8)
print(left_view(root))
print()
print(right_view(root))

            