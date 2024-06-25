# 1038. Binary Search Tree to Greater Sum Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root):
        self.val = 0
        self.sum_find(root, self.val)
        return root

    def sum_find(self, root, val):
        if root == None:
            return root
           
        value_1 = self.sum_find(root.right, self.val) 
        self.val += root.val
        root.val = self.val
        value_2 = self.sum_find(root.left, self.val) 


            


