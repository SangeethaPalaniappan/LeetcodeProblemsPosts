# 1207. Unique Number of Occurrences

class Solution:
    def uniqueOccurrences(self, arr):
        dic = {}
        for nums in arr:
            if nums not in dic:
                dic[nums] = 1
            else:
                dic[nums] += 1
        arr = []
        for num in dic.values():
            arr.append(num)
        sets = set(arr)
        if len(arr) != len(sets):
            return 0
        return 1        