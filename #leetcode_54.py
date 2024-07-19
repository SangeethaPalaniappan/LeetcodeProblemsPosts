# 54. Spiral Matrix

class Solution:
    def spiralOrder(self, matrix):
        i = 0
        j = len(matrix[0]) - 1
        k = len(matrix) - 1
        l = 0
        arr = []
        if len(matrix) == 1:
            return matrix[0]

        while i <= j and l <= k:
            var = l
            while var <= j:
                arr.append(matrix[i][var])
                var += 1
            i += 1 
            var = i
            
            while var <= k:
                arr.append(matrix[var][j])
                var += 1
            j -= 1  
            
            if i <= k:
                var = j
                
                while var >= l:
                    arr.append(matrix[k][var])
                    var -= 1
                k -= 1 
            if j >= l:
                var = k
            
                while var >= i:
                    arr.append(matrix[var][l])
                    var -= 1
                l += 1    
        return arr        
            
                
