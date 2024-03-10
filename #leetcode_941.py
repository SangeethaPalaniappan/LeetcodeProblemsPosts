#941. Valid Mountain Array

class Solution:
    def validMountainArray(self, arr):
        n = len(arr)
        if n < 3:
            return 0
        start = 0
        end = n - 1
        change = 0
        change_occur = 0
        while start < end and arr[start] < arr[start + 1]:
            start += 1
            change = 1
        while start < end and arr[end] < arr[end - 1]:
            end -= 1
            change_occur = 1
        if change == 1 and change_occur == 1:    
            if start == end:
                return 1    
        else:
            return 0    
                      