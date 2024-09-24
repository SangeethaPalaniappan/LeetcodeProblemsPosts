# 2269. Find the K-Beauty of a Number

class Solution:
    def divisorSubstrings(self, num, k):
        start = 0
        end = k
        count = 0
        n = num
        num = str(num)
        while end <= len(num):
            integer = int(num[start:end])
            if integer != 0 and n % integer == 0:
                count += 1
            start += 1
            end += 1
        return count
