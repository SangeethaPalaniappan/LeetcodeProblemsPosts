# 3115. Maximum Prime Difference

class Solution:
    def maximumPrimeDifference(self, nums):
        if len(nums) == 1:
            return 0

        start = 0
        end = len(nums) - 1
        while start <= end:
            if self.prime_check(nums[start]) == 1:
                break
            start += 1
        
        while start <= end:
            if  self.prime_check(nums[end]) == 1:
                break
            end -= 1
        return end - start            
    
    def prime_check(self, number):
        if number <= 1:
            return 0
        if number <= 3:
            return 1
        if number % 2 == 0 or number % 3 == 0:
            return 0
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return 0
            i += 6
        return 1    
