# 7. Reverse Integer

class Solution:
    def reverse(self, x):
        n = x
        val = 0
        if x < 0:
            x = -1 * x
        while x > 0:
            rem = x % 10
            val = val * 10 + rem
            x //= 10
        if val > 2147483648 or val < -2147483647:
            return 0
        if n > 0:
            return val
        return (-1 * val)
