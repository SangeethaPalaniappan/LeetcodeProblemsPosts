# 637. Average of Levels in Binary Tree

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root):
        q = deque()
        res = []
        if root != None:
            q.append(root)
        while len(q) != 0:
            tot = 0
            count = 0
            for i in range(len(q)):
                root = q.popleft()    
                tot += root.val
                count += 1
                if root.left != None:
                    q.append(root.left)
                if root.right != None:
                    q.append(root.right)
            avg = tot / count
            res.append(avg)
        return res                
