# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s):
        if s == " ":
            return 1
        arr = ""    
        for i in range(len(s)):
            char = s[i]
            if (ord(s[i]) >= 97 and ord(s[i]) <= 122) or (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 48 and ord(s[i]) <= 57):
                char = s[i].lower()
                arr += char
                
        start = 0
        end = len(arr) - 1
        while start < end:
            if arr[start] != arr[end]:
                return 0
            start += 1
            end -= 1    
        return 1    
