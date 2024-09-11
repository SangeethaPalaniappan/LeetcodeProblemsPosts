# 2220. Minimum Bit Flips to Convert Number

class Solution:
    def minBitFlips(self, start, goal):
        val = bin(start ^ goal)
        return val.count('1')
