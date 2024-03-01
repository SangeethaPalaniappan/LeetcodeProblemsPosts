# 67. Add Binary

class Solution:
    def addBinary(self, a, b):
        if a == "0" and b == "0":
            return a
        m = self.b_to_d(a)
        n = self.b_to_d(b)
        tot = m + n
        return self.d_to_b(tot)

    def b_to_d(self, n):
        sum = 0
        last = len(n) - 1
        for i in range(len(n)):

            sum += (int(n[last]) * (2 ** i))
            last -= 1
        return sum   

    def d_to_b(self, x):
        sum = ""
        while x > 0:
            rem = x % 2
            sum += str(rem)
            x //= 2
        return sum[::-1]            