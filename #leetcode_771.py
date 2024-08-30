# 771. Jewels and Stones

class Solution:
    def numJewelsInStones(self, jewels, stones):
        hashset = set()
        for i in jewels:
            hashset.add(i)
        count = 0
        for j in stones:
            if j in hashset:
                count += 1
        return count        
