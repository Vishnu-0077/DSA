class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def reverse_traversal(root):
    stack = []
    dup_stack = []
    stack.append(root)
    c=0
    while stack:
        for i in range(len(stack)):
            if c%2==0:
                node = stack.pop(0)
            else:
                node = stack.pop()
            print(node.data, end='')
            if c%2==0:
                if node.left:
                    dup_stack.append(node.left)
                if node.right:
                    dup_stack.append(node.right)
            else:
                if node.right:
                    dup_stack.append(node.right)
                if node.left:
                    dup_stack.append(node.left)
        c+=1
        for val in dup_stack:
            stack.append(val)
        dup_stack.clear()

    return

def zig_zag_traversal(root):
    stack = []
    dup_stack = []
    stack.append(root)
    c=1
    while stack:
        for i in range(len(stack)):
            node = stack.pop()
            print(node.data, end='')
            if c%2==0:
                if node.right:
                    dup_stack.append(node.right)
                if node.left:
                    dup_stack.append(node.left)
            else:
                if node.left:
                    dup_stack.append(node.left)
                if node.right:
                    dup_stack.append(node.right)
        
        c+=1
        for val in dup_stack:
            stack.append(val)
        dup_stack.clear()

    return
#just used brain and error adjustment







root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
zig_zag_traversal(root)

