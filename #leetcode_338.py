# 338. Counting  Bits

class Solution:
    def countBits(self, n):
        arr = [0] * (n + 1)
        for i in range(n + 1):
            count = 0
            k = i
            while i != 0:
                i = (i & i-1)
                count += 1
            arr[k] = count
        return arr    