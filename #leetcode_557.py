# 557. Reverse Words in a String III

class Solution:
    def reverseWords(self, s):
        length = len(s)
        m = 0
        n = 0
        s = list(s)
        while n < length:
            k = n    
            if n  == len(s) - 1 or s[n + 1] == " ":
                while n > m :    
                    s[m], s[n] = s[n], s[m]
                    n -= 1
                    m += 1
                
                n = k + 2
                m = n          
            else: 
                n += 1    
        arr = ""
        for i in s:
            arr += i
        return arr

