# 145. Binary Tree Postorder Traversal 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        arr = []
        self.traversal(arr, root)
        return arr
    
    def traversal(self, arr, root):
        if root == None:
            return root
        self.traversal(arr, root.left)
        self.traversal(arr, root.right)
        arr.append(root.val)
