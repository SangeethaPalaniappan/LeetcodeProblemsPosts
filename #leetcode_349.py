# 349. Intersection of Two Arrays

class Solution:
    def intersection(self, nums1, nums2):
        dic_1 = {}
        dic_2 = {}
        arr = []
        for i in nums1:
            if i not in dic_1:
                dic_1[i] = 1
        for j in nums2:
            if j not in dic_2:
                dic_2[j] = 1
        for k in dic_1.keys():
            if k in dic_2.keys():
                arr.append(k)        
  
        return arr                