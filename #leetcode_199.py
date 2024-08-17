# 199. Binary Tree Right Side View

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        q = deque()
        res = []
        if root != None:
            q.append(root)
        while len(q) != 0:
            val = 0
            for i in range(len(q)):
                root = q.popleft()
                val = root.val
                if root.left != None:
                    q.append(root.left)
                if root.right != None:
                    q.append(root.right)
            res.append(val)               
        return res    
