# 77. Combinations

class Solution:
    def combine(self, n, k):
        arr = []
        for i in range(1, n + 1):
            arr.append(i)
        emp_arr = []    
        main_arr = []
        self.func(0, k, arr, emp_arr, main_arr)
        return main_arr

    def func(self, i, k, arr, emp_arr, main_arr):
        if len(emp_arr) == k:
            sam = []
            for j in emp_arr:
                sam.append(j)
            main_arr.append(sam)
            return

        if i < len(arr):    
            first = arr[i]
            emp_arr.append(first)
            self.func(i + 1, k, arr, emp_arr, main_arr)
            emp_arr.pop()
            self.func(i + 1, k, arr, emp_arr, main_arr) 