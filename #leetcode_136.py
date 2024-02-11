# 136. Single Number

class Solution:
    def singleNumber(self, nums):
        integer = 0
        for num in nums:
            integer ^= num
        return integer
