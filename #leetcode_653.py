# 653. Two Sum IV - Input is a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root, k):
        hashmap = set()
        if self.recurse(root, hashmap, k) == 1:
            return 1
        return 0    
        
    def recurse(self, root, hashmap, target):    
        if root == None:
            return 0
        if root.val in hashmap:
            return 1
        sub = target - root.val
        hashmap.add(sub)
        
        k = self.recurse(root.left, hashmap, target)    
        if k == 1:
            return 1
        l = self.recurse(root.right, hashmap, target)
        if l == 1:
            return 1