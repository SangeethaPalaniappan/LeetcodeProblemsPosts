# 2108. Find First Palindromic String in the Array

class Solution:
    def firstPalindrome(self, words):

        for string in words:
            start = 0
            end = len(string) - 1
            while start <= end:
                if string[start] == string[end]:
                    start += 1
                    end -= 1
                else:
                    break
            else:
                return string            
        return ""        