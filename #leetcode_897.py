# 897. Increasing Order Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root):
        arr = []
        self.recursion(root, arr)
        
        temp = TreeNode(arr.pop())
        while len(arr) > 0:
            node = TreeNode(arr.pop())
            node.right = temp
            temp = node  
        return temp    

    def recursion(self, root, arr):
        if root == None:
            return root
        self.recursion(root.left, arr)    
        arr.append(root.val)
        self.recursion(root.right, arr)
