# 2697. Lexicographically Smallest Palindrome

class Solution:
    def makeSmallestPalindrome(self, s):
        if len(s) == 1:
            return s

        start = 0
        end = len(s) - 1
        string = list(s)

        while start <= end:
            if string[start] != string[end]:
                word = string[start]
                if string[end] < string[start]:
                    word = string[end]

                string[start] = word 
                string[end] = word
            start += 1
            end -= 1
           
        emp_str = ""    
        for char in string:
            emp_str += char
        return emp_str   
