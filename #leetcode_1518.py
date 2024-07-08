# 1518. Water Bottles

class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        count = numBottles
        while numBottles >= numExchange:
            div = numBottles // numExchange
            rem = numBottles % numExchange
            count += div
            numBottles = div + rem
        return count    
