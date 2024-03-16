# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s):
        a = s.split(" ")
        o = len(a)
        p = ""

        h = len(a)      

        for i in range(h // 2):
            a[i],a[h-1] = a[h - 1], a[i]
            h -= 1

        m = ""
        r=len(a)
        for i in range(r):
            if a[i]!="":    
                if i==r-1:
                    m=m+a[i]
                else:
                    m=m+a[i]+" "
    
            
        return m   
        
        
        
        
s = Solution()
s.reverseWords("the sky is blue")