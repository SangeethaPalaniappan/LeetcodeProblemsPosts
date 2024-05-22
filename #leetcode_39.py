# 39. Combination Sum

class Solution:
    def combinationSum(self, candidates, target):
        fin_arr = []
        
        def target_sum(start, tot, emp_arr):
            if len(candidates) <= start or tot > target:
                return
            if tot == target:
                fin_arr.append(emp_arr.copy())
                return
            for i in range(start, len(candidates)):
                emp_arr.append(candidates[i])
                
                target_sum(i, tot + candidates[i], emp_arr)
                
                emp_arr.pop()
       
        
        target_sum(0, 0, [])
        return fin_arr               