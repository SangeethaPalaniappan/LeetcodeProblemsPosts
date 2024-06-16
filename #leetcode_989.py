# 989. Add to Array-Form of Integer

class Solution:
    def addToArrayForm(self, num, k):
        integer = 0
        for i in num:
            integer = (integer * 10) + i
        
        tot = integer + k

        arr = []
        while tot != 0:
            rem = tot % 10
            tot //= 10
            arr.append(rem)
 
        start = 0
        end = len(arr) - 1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1  
        return arr   