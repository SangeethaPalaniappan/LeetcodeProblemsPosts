# 216. Contains Duplicate II

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                ind = hashmap[nums[i]]
                diff = i - ind
                if diff <= k:
                    return 1
                hashmap[nums[i]] = i    
        return 0                
                    
