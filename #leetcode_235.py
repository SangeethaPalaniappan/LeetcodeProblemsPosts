# 235. Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q) :
        if root.val == p.val or root.val == q.val:
            return root
        if (root.val > p.val and root.val < q.val) or (root.val > q.val and root.val < p.val):
            return root
        
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        return self.lowestCommonAncestor(root, p, q)                