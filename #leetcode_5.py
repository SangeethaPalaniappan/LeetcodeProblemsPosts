# 5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s):
        left, right = 0, 0
        length = 0
        maxi = 0
        word = ""
        word = s[0]
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    res_arr = s[i : j + 1]
                    rev = res_arr[::-1]
                    if res_arr == rev:
                        length = j - i + 1
                        if maxi < length:
                            maxi = length
                            word = res_arr
        return word                    
