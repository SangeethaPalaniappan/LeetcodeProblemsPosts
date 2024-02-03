class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = x
        rem = 0
        while x > 0:
            rem = (x % 10) + (rem * 10) 
            x = x // 10
        return s == rem
            