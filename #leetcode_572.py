# 572. Subtree of Another Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if root == None:
            return 0
        if root.val == subRoot.val:
            if self.check(root, subRoot) == 1:
                return 1  
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)   
        if left == 1 or right == 1:
            return 1 
        else:
            return 0    

    def check(self, root, subRoot):
        if root == None:
            if subRoot != None:
                return 0
        if root != None: 
            if subRoot == None:
                return 0
        if root == None and subRoot == None:
            return 1        
        if root.val != subRoot.val:
            return 0
        left = self.check(root.left, subRoot.left)
        right = self.check(root.right, subRoot.right)
        if left == 0 or right == 0:
            return 0
        else:
            return 1                
        
