# 2191. Sort the Jumbled Numbers

class Solution:
    def sortJumbled(self, mapping, nums):
        arr = []
        for i, n in enumerate(nums):
            res = 0
            if n == 0:
                res = mapping[n]
            prev = 1
            while n > 0:
                rem = n % 10
                res += (prev * mapping[rem]) 
                prev *= 10
                n //= 10
        
            arr.append((res, i))
        arr.sort()    
        res_arr = []
        for p in arr:
            res_arr.append(nums[p[1]])
        return res_arr
