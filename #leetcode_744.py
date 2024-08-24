# 744. Find Smallest Letter Greater Than Target

class Solution:
    def nextGreatestLetter(self, letters, target):
        i = 0
        ans = letters[0]
        while i < len(letters) and letters[i] == target:
            i += 1
        ans = letters[i]     
        return ans
