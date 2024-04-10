# 2073. Time Needed to Buy tickets


class Solution:
    def timeRequiredToBuy(self, tickets, k):
        n = len(tickets)
        steps = 0
        for i in range(n):
            if i <= k:
                if tickets[i] >= tickets[k]: 
                    steps += tickets[k]
                else:
                    steps += tickets[i]
            elif i > k:
                if tickets[i] >= tickets[k]:
                    steps += (tickets[k] - 1)            
                else:
                    steps += tickets[i]
        return steps               