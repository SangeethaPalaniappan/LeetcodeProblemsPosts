# 202. Happy Number

class Solution:
    def isHappy(self, n):
        
        if n == 1:
            return 1   
        if n < 4:
            return 0     
        tot = n
        hashmap = {}
        while tot > 1:
            fin = 0
            while n != 0:
                rem = n % 10
                n = n // 10
                root = rem ** 2
                fin += root

            if fin not in hashmap:
                hashmap[fin] = 1
            elif fin in hashmap:
                return 0    
            tot = fin
            n = tot

            if n == 1:
                break
            if n < 4:
                return 0     
        return tot
