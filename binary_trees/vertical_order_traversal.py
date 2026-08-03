class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def vertical_traversal(root):
    verticals = {}
    verticals[root.data] = 0
    queue = []
    result = []
    queue.append(root)
    while queue:
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                verticals[node.left.data] = verticals[node.data] - 1
            if node.right:
                queue.append(node.right)
                verticals[node.right.data] = verticals[node.data] + 1

    sorted_dic = sorted(verticals.items(), key = lambda x: x[1])

    for i in sorted_dic:
        print(i[0], end=" ")
    #this is just for printing whatever we got

def vertical_traversal_double_queue(root):
    queue = []
    verticals = {}
    queue.append([root,0])
    while queue:
        for i in range(len(queue)):
            node, ind = queue.pop(0)
            if node.left:
                queue.append([node.left, ind-1])
            if node.right:
                queue.append([node.right, ind+1])
            if ind in verticals:
                verticals[ind].append(node.data)
            else:
                verticals[ind] = [node.data]
    sorted_dic = dict(sorted(verticals.items(), key = lambda x: x[0]))
    return list(sorted_dic.values())
            
    
        

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
vertical_traversal(root)
print()
print(vertical_traversal_double_queue(root))