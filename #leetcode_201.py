# 201. Bitwise AND of Numbers Range

class Solution:
    def rangeBitwiseAnd(self, left, right):

        while right > left:
            right &= (right - 1)
        return right