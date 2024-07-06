# 746. Min Cost Climb Stairs

class Solution:
    def minCostClimbingStairs(self, cost):
        hashmap = {}
        return min(self.recursive(cost, 0, hashmap), self.recursive(cost, 1, hashmap))

    def recursive(self, cost, ind, hashmap):
        if ind in hashmap:
            return hashmap[ind]
        if ind >= len(cost):    
            return 0
        mini = float('inf')
        val1 = self.recursive(cost, ind + 1, hashmap) + cost[ind] 
        if val1 < mini: 
            mini = val1   
        val2 = self.recursive(cost, ind + 2, hashmap) + cost[ind]   
        if val2 < mini: 
            mini = val2 
        hashmap[ind] = mini
        return mini 
