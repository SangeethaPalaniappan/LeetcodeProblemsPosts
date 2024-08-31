# 997. Find the Town Judge

class Solution:
    def findJudge(self, n, trust):
        count = 0
        arr = [0] * (n + 1)

        for arr_t in trust:
            arr[arr_t[0]] -= 1
            arr[arr_t[1]] += 1
        for i in range(1, n + 1):
            if arr[i] == n - 1:
                return i
        return -1            
