# 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices):
        profit = 0
        first = 0 
        second = 0
        while second < len(prices): 
            if prices[first] >= prices[second]:
                first = second
            else:
                diff = prices[second] - prices[first]
                profit += diff
                first = second
            second += 1
        return profit
