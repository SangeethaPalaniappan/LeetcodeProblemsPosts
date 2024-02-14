# 389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lis = sorted(s)
        lis1 = sorted(t)
        for i in range(len(lis)):
            if lis[i] != lis1[i]:
                return lis1[i]
        return lis1[len(lis1) - 1]
