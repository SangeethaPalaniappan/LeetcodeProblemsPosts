# 605. Can Place Flowers

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed) - 1):
            if n == 0:
                break
            if flowerbed[i] == 0:
                if i == 0:
                    if flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1

                else:
                    if flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
        if n != 0:
            if  flowerbed[len(flowerbed) - 1] == 0:
                if flowerbed[len(flowerbed) - 2] == 0:
                    flowerbed[len(flowerbed) - 1] = 1
                    n -= 1                
        if n == 0:
            return 1
        return 0    
