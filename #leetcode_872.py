# 872. Leaf-Similar Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []

    def leafSimilar(self, root1, root2):
        self.finding_similar_leaves(root1)
        arr_1 = self.arr
        print(self.arr)
        self.arr = []

        self.finding_similar_leaves(root2)
        print(self.arr)
        arr_2 = self.arr
        if arr_1 == arr_2:
            return 1
        else:
            return 0

    def finding_similar_leaves(self, root):
        if root.left != None:
            self.finding_similar_leaves(root.left)
        elif root.left == None and root.right == None:
            self.arr.append(root.val)
            return self.arr                
        if root.right != None:
            self.finding_similar_leaves(root.right) 

    