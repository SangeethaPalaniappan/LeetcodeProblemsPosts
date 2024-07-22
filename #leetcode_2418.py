# 2418. Sort the People

class Solution:
    def sortPeople(self, names, heights):
        if len(heights) == 1:
            return names
        hashmap = {}
        for i in range(len(heights)):
            hashmap[heights[i]] = names[i]   
        heights.sort(reverse = True)
        for k in range(len(heights)):
            names[k] = hashmap[heights[k]]
        return names    
