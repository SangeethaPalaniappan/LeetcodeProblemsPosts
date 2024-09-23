# 1281. Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n):
        m = n
        pro_ans = 1
        sum_ans = 0
        while m != 0:
            rem = m % 10
            pro_ans *= rem
            sum_ans += rem
            m //= 10
        return (pro_ans - sum_ans)
