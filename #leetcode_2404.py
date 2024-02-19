# 2404. Most Frequent Even Element

class Solution:
    def mostFrequentEven(self, nums):
        dic = {}
        i = 0

        while i < len(nums):
            if nums[i] % 2 == 0:
                if nums[i] not in dic:
                    dic[nums[i]] = 1
                else:
                    dic[nums[i]] += 1            
            i += 1 
              
        if dic == {}:
            return -1
               
        r = max(dic.values())
        s = max(dic.keys())

  
        for j in dic.keys():
            if j < s and dic.get(j) == r: 
                s = j
        return s





