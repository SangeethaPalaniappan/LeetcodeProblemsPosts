# 1122. Relative Sort Array
class Solution:
    def relativeSortArray(self, arr1, arr2):
        hashmap = {}
        for i in arr1:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        arr = []
        dup = []

        for l in arr2:
            if l in hashmap:
                for i in range(hashmap[l]):
                    arr.append(l)
                hashmap[l] = 0
        for j in hashmap:
            if hashmap[j] > 0:
                for i in range(hashmap[j]):
                    dup.append(j)
                          
     
        dup.sort()
        arr.extend(dup)
  
        return arr
                    
