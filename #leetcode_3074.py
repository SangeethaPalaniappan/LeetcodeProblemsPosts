# 3074. Apple Redistribution into Boxes

class Solution:
    def minimumBoxes(self, apple, capacity):
        count = 0
        tot = sum(apple)
        capacity.sort(reverse = True)
        sums = 0
        n = 0
        end = len(capacity)
        while n < end:
            if sums < tot:
                count += 1
                sums += capacity[n]
                n += 1
            else:
                return count
        return count    