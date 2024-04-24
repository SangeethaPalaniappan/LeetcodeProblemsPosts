# 1137. Nth Tribonacci Number

class Solution:
    def tribonacci(self, n):
        dic = {}
        dic[0] = 0
        dic[1] = 1
        dic[2] = 1
        for i in range(3, n + 1):
            dic[i] = dic[i - 1] + dic[i - 2] + dic[i - 3]
        return dic[n]    