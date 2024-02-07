class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxi = max(candies)

        
        for candy in range(len(candies)):
            if (candies[candy] + extraCandies) >= maxi:
                candies[candy] = 1
            else:
                candies[candy] = 0    
        return candies            
