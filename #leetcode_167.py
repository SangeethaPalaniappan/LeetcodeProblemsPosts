# 167. Two Sum II - Input Array is Sorted

class Solution:
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        while i < j:
            sums = numbers[i] + numbers[j]
            if sums < target:
                i += 1
            elif sums > target:
                j -= 1
            if sums == target:
                return (i + 1), (j + 1)
                break



