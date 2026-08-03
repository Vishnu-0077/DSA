class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bottom_view(root):
    queue = [[root,0]]
    verticals = {}
    while queue:
        for i in range(len(queue)):
            node, ind = queue.pop(0)
            if node.left:
                queue.append([node.left, ind-1])
            if node.right:
                queue.append([node.right, ind+1])
            if ind not in verticals:
                verticals[ind] = [node.data]
            else:
                verticals[ind].append(node.data)
    sorted_dic = dict(sorted(verticals.items(), key = lambda x: x[0]))
    list_dic = list(sorted_dic)
    bottom_view = []
    for i in list_dic:
        bottom_view.append(sorted_dic[i][-1])
    return bottom_view


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(bottom_view(root))