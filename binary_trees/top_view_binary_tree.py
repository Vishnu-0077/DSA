class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def top_view(root):
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
            if ind not in verticals:
                verticals[ind] = node.data
            else:
                continue
    sorted_dic = dict(sorted(verticals.items(), key = lambda x: x[0]))
    '''
            for value in sorted(mpp.items()):
            ans.append(value[1])
            
            can use this also instead of above bullshit'''
    
    return list(sorted_dic.values())




root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right = Node(3)
root.right.right = Node(11)
root.right.left = Node(9)
print(top_view(root))