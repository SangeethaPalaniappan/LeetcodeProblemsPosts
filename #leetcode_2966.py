# 2966. Divide Array Into Arrays With Max Difference

class Solution:
    def divideArray(self, nums, k):
        nums.sort()
        mat = []
        i = 0
        while i < len(nums) - 2:
            j = i
            mat.append(nums[j : j + 3])
            i = j + 3
        for arr in range(len(mat)):
            if (mat[arr][1] - mat[arr][0] <= k) and (mat[arr][2] - mat[arr][1] <= k) and (mat[arr][2] - mat[arr][0] <= k):
                continue
            else:
                return []    
        return mat        
