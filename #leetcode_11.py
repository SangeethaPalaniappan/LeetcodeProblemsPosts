# 11. Container With Most Water

class Solution:
    def maxArea(self, heights):
        maxi = 0
        start = 0
        end = len(heights) - 1
        while start < end:
            diff = end - start
            mini = min(heights[start], heights[end])
            val = diff * mini
            if val > maxi:
                maxi = val
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1        
        return maxi        