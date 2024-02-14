# 2149. Rearrange Array Elements by Sign

class Solution:
    def rearrangeArray(self, nums):
        pos_arr = []
        neg_arr = []
        for integer in nums:
            if integer > 0:
                pos_arr.append(integer)
            elif integer < 0:
                neg_arr.append(integer)   

        ind = 0  
        for i in range(len(pos_arr)):
            nums[ind] = pos_arr[i]
            ind += 1
            nums[ind] = neg_arr[i]
            ind += 1     
        return nums    