# 3005. Count Elements with Maximum Frequency

class Solution:
    def maxFrequencyElements(self, nums):
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        maxi = max(dic.values())
        count = 0
        for value in dic.values():
            if maxi == value:
                count += maxi
        return count        