# 48. Rotate Image
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):    
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 

        for i in range(len(matrix)):
            matrix[i].reverse()


        