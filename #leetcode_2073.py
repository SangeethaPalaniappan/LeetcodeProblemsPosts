# 2073. Time Needed to Buy Tickets

class Solution:
    def timeRequiredToBuy(self, tickets, k):
        start = 0
        end = len(tickets)
        count = 0
        while start < end:
            if tickets[start] > 0:
                tickets[start] -= 1
                if start == k and tickets[start] == 0:
                    return count + 1 
                
                
                count += 1        
                
            start += 1 
            if start == end:
                start = 0       
                    
 