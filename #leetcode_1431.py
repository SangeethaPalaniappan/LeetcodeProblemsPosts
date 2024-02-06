class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxi = max(candies)
        
        start = 0
        end = len(candies) - 1
        

        while start <= end:    
            p = candies[start] + extraCandies
            q = candies[end] + extraCandies
            if p >= maxi :
                candies[start] = 1

            else:
                candies[start] = 0    
            if q >= maxi :
                candies[end] = 1  
                 
            else:
                candies[end] = 0
            start += 1
            end -= 1    
        return candies            
