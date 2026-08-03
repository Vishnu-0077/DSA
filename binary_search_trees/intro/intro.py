class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None


def find_node_recursion(req_value,root):
    if root is None:
        return None
    if root.data==req_value:
        return root
    if req_value<root.data:
        return find_node_recursion(req_value, root.left)
    if req_value>root.data:
        return find_node_recursion(req_value, root.right)

def find_node_interative(req_value, root):
    while root is not None:
        if root.data == req_value:
            return root
        if req_value<root.data:
            root = root.left
        if req_value>root.data:
            root = root.right

    return None    

if __name__ == "__main__":
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.left = Node(9)
    root.right.right = Node(14)

    print(find_node_recursion(9,root))
    print(find_node_interative(9, root))


    