# 1078. Occurrences After Bigram

class Solution:
    def findOcurrences(self, text, first, second):
        arr = text.split(" ")
        result_arr = []
        for i in range(len(arr) - 2):
            if arr[i] == first and arr[i + 1] == second:
                result_arr.append(arr[i + 2])
        return result_arr     
    