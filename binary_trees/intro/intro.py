class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None

    def  preorder(self, start, traversal):
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal
    def inorder(self, start, traversal):
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.inorder(start.right, traversal)
        return traversal
    def postorder(self, start, traversal):
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.data) + "-")
        return traversal
    def levelorder(self, start):
        level_order = []
        queue = []
        queue.append(start)
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_order.append(level)
        return level_order
    
    #draw and see how level order works, eassyy only

    def preorder_traversel_iterative(self,start):
        stack = []
        stack.append(start)
        while stack:
            node = stack.pop()
            print(node.data,end="")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return
    def level_order_traversel_iterative(self,start): #see the difference between the interative level order and iterative preorder, they both areextremely similar only with sall changes
        stack = []
        stack.append(start)
        while stack:
            node = stack.pop(0) #way we pop changes, and 
            print(node.data,end="")
            if node.left: #the order we append changes
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return
    def inorder_iterative_traversel(self,start):
        stack = []
        node = start
        while stack or node:
            while node: #while node is not None, we keep going left, if none, this loop does not execute, so we can go higher
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.data,end="")
            node = node.right #if we are almost at left end, then right is None, so we pop the stack and print the node, then we go to the right// actually node.right.. help us to not comback there again, if node.right not written, we will comback there again
        return stack
    
    def postorder_iterative_traversel(self,start):
        stack = []
        node = start
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.data,end="")
            if stack and stack[-1].right!=None: 
                node = stack[-1].right #if we have a right child, we go to it, else we pop the stack and print the node, then we go to the right
            else:
                node = None
        return stack
                
            
            
bt=BinaryTree()
bt.root = Node("A")
bt.root.left = Node("B")
bt.root.right = Node("C")
bt.root.left.left = Node("D")
bt.root.left.right = Node("E")
bt.root.right.left = Node("F")
bt.root.right.right = Node("G")
print(bt.preorder(bt.root,""))
print(bt.inorder(bt.root,""))
print(bt.postorder(bt.root,""))
print(bt.levelorder(bt.root))
print(bt.preorder_traversel_iterative(bt.root))
print(bt.level_order_traversel_iterative(bt.root))
print(bt.inorder_iterative_traversel(bt.root))
# The above code implements a binary tree with various traversal methods including preorder, inorder, postorder, and level order traversals.
# It also includes iterative versions of preorder, inorder, and postorder traversals. 
# The binary tree is constructed with nodes labeled A to G for demonstration purposes.