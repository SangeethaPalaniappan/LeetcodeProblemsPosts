# 1387. Sort Integers by the Power Value

class Solution:
    def getKth(self, lo, hi, k):
        hashmap = {}
        map_values = {}
        for i in range(lo, hi + 1):
            val = self.find_power(i, hashmap, 0)
            map_values[i] = [i, val]  
            hashmap[i] = val
            
        values = list(map_values.values())
        res = sorted(values, key = lambda values :values[1])
        return res[k - 1][0]   
        
    def find_power(self, n, hashmap, tot):
        if n in hashmap:
            return hashmap[n]+ tot
        if n == 1:
            return tot
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n) + 1 
               
        tot = self.find_power(n, hashmap, tot + 1)
        return tot 
