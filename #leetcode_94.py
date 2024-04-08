# 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        arr = []
        return self.bit(root, arr)

    
    def bit(self, root, arr):
        if root == None:
            return arr
            
        if root.left != None:
            self.bit(root.left, arr)  

        arr.append(root.val)

        if root.right != None:
            self.bit(root.right, arr)
            
        return arr