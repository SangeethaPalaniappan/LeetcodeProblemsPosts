# 100. Same Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        temp_1 = p        
        temp_2 = q
        if temp_1 == None:
            if temp_2 == None:
                return 1
            else:
                return 0
        if temp_2 == None:
            if temp_1 == None:
                return 1
            else:
                return 0        
        if temp_1.val == temp_2.val:
            if self.isSameTree(p.left, q.left) == 1:
                if self.isSameTree(p.right, q.right) == 1:
                    return 1
                else:
                    return 0
            else:
                return 0            
        else:
            return 0