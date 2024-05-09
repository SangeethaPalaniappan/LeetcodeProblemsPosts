# 3075. Maximize Happiness of Selected Children

class Solution:
    def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse = True)
        tot = 0
        i = 0
        end = len(happiness) - 1
        start = 0
        while start <= end and k != 0:
            happiness[start] -= i
            if happiness[start] > 0:
                tot += happiness[start]
                i += 1
                start += 1
                k -= 1
            else:
                return tot
        return tot    