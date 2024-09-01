# 2022. Convert 1D Array Into 2D Array

class Solution:
    def construct2DArray(self, original, m, n):
        if len(original) > m * n or m * n > len(original):
            return []
        matrix = []
        ind = 0
        for i in range(m):
            arr = []
            for j in range(n):
                arr.append(original[ind])
                ind += 1
            matrix.append(arr)    
        return matrix        
