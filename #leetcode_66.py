class Solution:
    def plusOne(self, digits):
        last = len(digits) - 1
        while last >= 0:
            if digits[last] < 9:
                digits[last] += 1
                return digits
            digits[last] = 0
            last -= 1    
        digits[0] = 1
        digits.append(0)
        return digits