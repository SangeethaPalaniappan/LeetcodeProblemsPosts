# 917. Reverse Only Letters

class Solution:
    def reverseOnlyLetters(self, s):
        start = 0
        end = len(s) - 1
        lis = list(s)
        while start < end:
            while start < end and not (ord(s[start]) >= 65 and ord(s[start]) <= 90 or ord(s[start]) >= 97 and ord(s[start]) <= 122):
                
                start += 1
            while start < end and not(ord(s[end]) >= 65 and ord(s[end]) <= 90 or ord(s[end]) >= 97 and ord(s[end]) <= 122): 
                end -= 1

            lis[start], lis[end] = lis[end], lis[start]

            start += 1
            end -= 1
        fin_str = ""
        for char in lis:
            fin_str += char    
        return fin_str            

