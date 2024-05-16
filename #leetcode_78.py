# 78. Subsets

class Solution:
    def subsets(self, nums):
        emp_arr = []
        main_arr = [[]]
        i = 0
        self.func(i, nums, emp_arr, main_arr)
        return main_arr


    def func(self, i, arr, emp_arr, main_arr):
        if len(arr) == 0:
            return
        first = arr[i]
        emp_arr.append(first)
        sample = []
        for j in emp_arr:
            sample.append(j)
        main_arr.append(sample)
        self.func(i, arr[i + 1 :], emp_arr, main_arr)
        emp_arr.pop()
        self.func(i, arr[i + 1 :], emp_arr, main_arr)


