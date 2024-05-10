# 786. Kth Smallest Prime Fraction

class Solution:
    def kthSmallestPrimeFraction(self, arr, k: int):
        if len(arr) == 2:
            return arr
        dic = {}
        num = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                frac = arr[i] / arr[j]
                if frac not in dic:
                    dic[frac] = [arr[i], arr[j]]
                else:
                    if dic[frac][0] > arr[i] or dic[frac][1] > arr[j]:
                        dic[frac] = [arr[i], arr[j]]
                num.append(frac)  
            
        set_num = list(set(num))
        
        set_num.sort()
        
        value = dic[set_num[k - 1]]
        
        return value                  
                