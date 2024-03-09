# 2540. Minimum Common Value

class Solution:
    def getCommon(self, nums1, nums2):
        point_1 = 0
        point_2 = 0
        while point_1 < len(nums1) and point_2 < len(nums2):
            if nums1[point_1] < nums2[point_2]:
                point_1 += 1
            elif nums1[point_1] > nums2[point_2]:
                point_2 += 1
            elif point_1 < len(nums1) and point_2 < len(nums2) and nums1[point_1] == nums2[point_2]:
                return nums1[point_1]     
        while point_1 < len(nums1) and point_2 == len(nums2) - 1:
            if nums1[point_1] < nums2[point_2]:
                point_1 += 1
            if nums1[point_1] == nums2[point_2]:
                return nums1[point_1]       
            else:
                break    
        while point_2 < len(nums2) and point_1 == len(nums1) - 1:
            if nums1[point_1] > nums2[point_2]:
                point_2 += 1  
            if nums1[point_1] == nums2[point_2]:
                return nums1[point_1]     
            else:
                break                    
        return -1                                               