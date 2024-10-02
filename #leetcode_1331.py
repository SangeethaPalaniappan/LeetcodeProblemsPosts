# 1331. Rank Transform of an Array

class Solution:
    def arrayRankTransform(self, arr):
        sorted_arr = arr.copy()
        sorted_arr.sort()
        hashmap = {}
        j = 1
        for i in range(len(sorted_arr)):
            if sorted_arr[i] not in hashmap:
                hashmap[sorted_arr[i]] = j
                j += 1
        for k in range(len(arr)):
            arr[k] = hashmap[arr[k]]
        return arr
