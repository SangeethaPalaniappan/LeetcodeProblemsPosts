# 2053. Kth Disting String in an Array

class Solution:
    def kthDistinct(self, arr, k):
        l = 0
        hashmap = {}
        for i in arr:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        for j in hashmap:            
            if hashmap[j] == 1:
                l += 1
                if k == l:
                    return j
                      
        return ""
