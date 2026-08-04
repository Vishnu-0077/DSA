class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_sum_in_height(root):
    if not root:
        return 0
    return root.value + max(max_sum_in_height(root.left), max_sum_in_height(root.right))
def max_any_path_sum(root,stack = None):
    if stack is None:
        stack = []
    if not root:
        return stack[-1]
    sum_left = max_sum_in_height(root.left)
    sum_right = max_sum_in_height(root.right)

    total_sum = sum_left + sum_right + root.value
    if stack and total_sum>stack[-1]:
        stack.pop()
        stack.append(total_sum)
    if not stack:
        stack.append(total_sum)
    
    return max(max_any_path_sum(root.left,stack) , max_any_path_sum(root.right,stack))

def max_path_sum_2(root):
    if root is None:
        return 0
    max_p = root.value+max_sum_in_height(root.left)+max_sum_in_height(root.right)
    return max(max_path_sum_2(root.left),max_path_sum_2(root.right),max_p)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(max_any_path_sum(root))
print(max_path_sum_2(root))
