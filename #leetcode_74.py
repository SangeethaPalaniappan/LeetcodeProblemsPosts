# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix, target):    
        start = 0
        end = (len(matrix) * len(matrix[0])) - 1
        row_len = len(matrix[0])

        while start <= end:
            mid = (start + end) // 2
            row = mid // row_len
            column = mid % row_len

            if matrix[row][column] == target:
                return 1
            if matrix[row][column] > target:
                end = mid - 1
            else:
                start = mid + 1
        return 0                
