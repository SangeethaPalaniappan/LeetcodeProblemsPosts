# 104. Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        count = 0
        maxi = 0
        return self.find_depth(root, count, maxi)
        
    def find_depth(self, root, count, maxi):  
        if root == None:
            maxi = max(maxi, count)
            return maxi
        maxi = max(self.find_depth(root.left, count + 1, maxi), self.find_depth(root.right, count + 1, maxi))
        return maxi
