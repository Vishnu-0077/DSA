class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#i think we can do again by the height of the tree and recursion
from queue import Queue
def height_of_tree(root):
    if not root:
        return 0
    q=Queue()
    q.put(root)
    height=0
    while not q.empty():
        size = q.qsize()
        for i in range(size):
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        height +=1
    
    return height

def diameter_of_tree(root,max_height = 0):

    if not root:
        return max_height+1 #so it includes both sides

    node_left = root.left
    node_right = root.right

    height_left = height_of_tree(node_left)
    height_right = height_of_tree(node_right)

    height = height_left + height_right #this height updating can be done is different mathod, can also done using stacks

    if height>max_height:
        max_height = height
    
    return max(diameter_of_tree(node_left,max_height),diameter_of_tree(node_right,max_height))

#draw and visualize to understand, adhan ore vali

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.right.left = Node(7)
root.left.right.right = Node(8)
print(diameter_of_tree(root))



