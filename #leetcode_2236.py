# 2236. Root Equals Sum of Children

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root):
        child_sum = root.left.val + root.right.val
        if root.val == child_sum:
            return 1
        return 0    