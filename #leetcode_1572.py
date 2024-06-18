# 1572. Matrix Diagonal Sum

class Solution:
    def diagonalSum(self, mat):
        tot = 0
        i = 0
        l = len(mat) - 1
        while i < len(mat) and l >= 0:
            first = mat[i][i]
            second = mat[i][l]
            if i == l:
                tot += first
            else: 
                tot += (first + second)   
                
            i += 1
            l -= 1
        return tot    