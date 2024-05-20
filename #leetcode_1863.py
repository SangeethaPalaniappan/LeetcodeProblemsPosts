# 1863. Sum of All Subset XOR Totals

class Solution:
    def subsetXORSum(self, nums):
        tot = 0
        emp_arr = []
        fin_arr = []
        self.recurse(0, nums, 0, fin_arr, emp_arr)
        return sum(fin_arr)
    def recurse(self, i, gn_arr, tot, fin_arr, emp_arr):
        if len(gn_arr) == 0:
            fin_arr.append(tot)
            return
        if i < len(gn_arr):    
            first = gn_arr[i]    
            tot ^= first    
            emp_arr.append(first)
            self.recurse(i, gn_arr[i + 1:], tot, fin_arr, emp_arr)
            emp_arr.pop()
            tot = tot ^ first
            self.recurse(i, gn_arr[i + 1:], tot, fin_arr, emp_arr)