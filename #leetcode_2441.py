# 2441. Largest Positive Integer That Exists With Its Negative

class Solution:
    def findMaxK(self, nums):
        dic = set()
        arr = []
        change = 0
        for i in nums:
            integer = -1 * i
            if integer not in dic:
                dic.add(i)
            else:
                arr.append(abs(i))
                change = 1
            
        if change == 1:
            return max(arr)
        return -1            