# 700. Search in a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val):
        if root == None:
            return root
        else:
            if val == root.val:
                return root
            elif val < root.val:
                root = root.left
                return self.searchBST(root , val)
                
            elif val > root.val:
                root = root.right
                return self.searchBST(root , val)
                
            
        
            