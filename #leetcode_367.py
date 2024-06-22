# 367. Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num):
        left = 1
        right = num // 2
        if num == 1:
            return 1
        while left <= right:
            mid = (left + right) >> 1
            val = mid * mid
            if val == num:
                return 1
            elif val > num:
                right = mid - 1
            else:
                left = mid + 1
        return 0                
