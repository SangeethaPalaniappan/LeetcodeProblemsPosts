# 441. Arranging Coins

class Solution:
    def arrangeCoins(self, n):
        pos = 1
        tot = 0
        while n > 0:
            n -= pos
            pos += 1
            if n >= 0:
                tot += 1

        return tot            
