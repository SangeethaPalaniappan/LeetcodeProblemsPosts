#2706. Buy Two Chocolates

class Solution:
    def buyChoco(self, prices, money):
        mini = min(prices)
        index = prices.index(mini)
        prices[index] = inf
        mini_1 = min(prices)
        chocolates = mini + mini_1
        if chocolates <= money:
            return money - chocolates
        return money    