class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def construct_bst(preorder):
    index = [0]  # mutable index

    def helper(min_val, max_val):
        if index[0] == len(preorder):
            return None

        val = preorder[index[0]]
        if val < min_val or val > max_val:
            return None

        index[0] += 1
        root = Node(val)
        root.left = helper(min_val, val)
        root.right = helper(val, max_val)
        return root

    return helper(float('-inf'), float('inf'))

print(construct_bst([10, 5, 1, 7, 40, 50]))
