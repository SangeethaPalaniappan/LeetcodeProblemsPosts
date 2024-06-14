# 278. First Bad Version

# The isBadVersion API is already defined for you.
def isBadVersion(version, n):
    if n == version:
        return 1
    return 0

class Solution:
    def firstBadVersion(self, n):
        start = 1
        end = n
        while start <= end:
            n = (start + end) // 2
            bv = isBadVersion(n)
            if bv == 0:
                start = n + 1
            else:
                end =  n -1   
        return start     
