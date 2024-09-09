# 575. Distribute Candies

class Solution:
    def distributeCandies(self, candyType):
        hashtable = set()
        for i in candyType:
            hashtable.add(i)

        n = len(candyType)  
        m = len(hashtable)      
        if m < n // 2:
            return m
        else:
            return n // 2                
