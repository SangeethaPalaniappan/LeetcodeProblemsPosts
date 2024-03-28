# 404. Sum of Left Leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root):
        sum = 0
        if root.left == None and root.right == None:
            return sum
        return self.find_sum(root, sum, 0)
        
        
    def find_sum(self, root, sum, k):
        if root == None:
            return sum

        if root.left == None and root.right == None:
            if k == 0:
                sum += root.val
            return sum

        k = 0
        sum = self.find_sum(root.left, sum, k)
        
        if root.right != None:
            k = 1
            sum = self.find_sum(root.right, sum, k)     
        return sum