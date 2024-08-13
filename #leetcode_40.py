# 40. Combination Sum II

class Solution:
    def combinationSum2(self, candidates, target):
        res_arr = []
        candidates.sort()
        self.calculate(candidates, target, res_arr, 0, [])
        return res_arr

    def calculate(self, arr, target, res_arr, ind, comb_arr):
        if target < 0:
            return None
        if target == 0:
            res_arr.append(comb_arr)
            return 

        for i in range(ind, len(arr)):
            if i > ind and arr[i] == arr[i - 1]:
                continue
            self.calculate(arr, target - arr[i], res_arr, i + 1, comb_arr + [arr[i]])
    
