# 1550. Three Consecutive Odds

class Solution:
    def threeConsecutiveOdds(self, arr):
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                return 1
        return 0            