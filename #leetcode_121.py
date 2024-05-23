# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices):
        if len(prices) == 1:
            return 0
        maxi = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[left] < prices[right]:
                diff = prices[right] - prices[left]
                if diff > maxi:
                    maxi = diff
   
            elif prices[left] > prices[right]: 
                left = right
            right += 1       
        return maxi        