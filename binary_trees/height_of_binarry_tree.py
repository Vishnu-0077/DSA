class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def height_of_binary_tree_stack_method(root):
    stack = []
    stack.append(root)
    height = 0
    while stack:
        for i in range(len(stack)):
            node=stack.pop(0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        height+=1
    return height

from queue import Queue

def height_of_binary_tree_queue_method(root):
    queue = Queue()
    queue.put(root)
    height = 0
    while not queue.empty():
        for i in range(queue.qsize()):
            node = queue.get() #it is same as ...node = stack.pop()
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
        height+=1
    return height
            
'''
both define statement are same but done using the queue and other is stack which uses queue
'''

def height_using_recusion(root):
    if not root:
        return 0
    return 1 + max(height_using_recusion(root.left), height_using_recusion(root.right))

    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(height_of_binary_tree_stack_method(root))
print(height_of_binary_tree_queue_method(root))
print(height_using_recusion(root))
    
    


