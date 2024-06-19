# 144.  Binary Tree Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        arr = []
        self.traversal(arr, root)
        return arr
    
    def traversal(self, arr, root):
        if root == None:
            return root
        arr.append(root.val)
        self.traversal(arr, root.left)
        self.traversal(arr, root.right)

            