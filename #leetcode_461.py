# 461. Hamming Distance

class Solution:
    def hammingDistance(self, x, y):
        s = x ^ y
        count = 0
        while s > 0:
            rem = s % 2
            s = s // 2
            if rem == 1:
                count += 1
        return count
