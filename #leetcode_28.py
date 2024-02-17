class Solution:
    def strStr(self, haystack, needle):
        length, l= len(needle),  len(haystack)
        
        for k in range(l) :
            if haystack[k : length + k] == needle:
                return k    
        return -1

