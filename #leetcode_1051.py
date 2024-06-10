# 1051. Height Checker

class Solution:
    def heightChecker(self, heights):
        s = heights.copy()
        heights.sort()
        count = 0 
        for i in range(len(heights)):
            if heights[i] != s[i]:
                count += 1
        return count        