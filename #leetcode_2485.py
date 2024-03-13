# 2485. Find the Pivot Integer

class Solution:
    def pivotInteger(self, n):
        tot = ((n * n) + n)// 2
        sqr = int(sqrt(tot))
        if tot == (sqr * sqr):
            return sqr
        return -1    