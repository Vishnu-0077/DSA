# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def high(root):
            if root is None:
                return float('-inf')
            pick = root.val
            no_pick = 0
            if root.left or root.right:
                pick = root.val + max(high(root.left),high(root.right))
                no_pick = root.val
            return max(pick,no_pick)
            
        def maxi_sum(root):
            if root is None:
                return float('-inf')
            maxi = root.val + (high(root.left) if root.left else 0) + (high(root.right) if root.right else 0)
            return max(maxi,maxi_sum(root.left),maxi_sum(root.right))
        
        return maxi_sum(root)