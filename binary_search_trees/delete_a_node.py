class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findMin(node):
    while node.left:
        node = node.left
    return node

def delete(root, key):
    if root is None:
        return None

    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        # Case 1: no child
        if root.left is None and root.right is None:
            return None #here both the child are None so we can just directly set it to None
        # Case 2: one child
        if root.left is None: #here and the below one there is only one of them that is None so set the other one to be the one
            return root.right
        elif root.right is None:
            return root.left
        # Case 3: two children
        temp = findMin(root.right) #find the minimum of the right subtree and just replace the root value, 
        root.data = temp.data
        root.right = delete(root.right, temp.data) # and now u delete the duplicate in the right subtree which was originally present

    return root


node = Node(8)
node.left = Node(3)
node.right = Node(10)
node.left.left = Node(1)
node.left.right = Node(6)
node.right.left = Node(9)
node.right.right = Node(14)
print(delete(node, 10))
    



    