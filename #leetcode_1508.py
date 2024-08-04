# 1508. Range Sum of Sorted Subarray Sums

class Solution:
    def rangeSum(self, nums, n, left, right):
        tot = 0
        res_arr = []
        for i in range(len(nums)):
            arr = []
            for j in range(i, len(nums)):
                arr.append(nums[j]) 
                res_arr.append(sum(arr))
        res_arr.sort()    
        val = sum(res_arr[left - 1 : right])     
        if val > 1000000007:
            val = val % 1000000007
        return val
