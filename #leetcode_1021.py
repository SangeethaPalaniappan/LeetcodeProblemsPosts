# 1021. Remove Outermost Parentheses

class Solution:
    def removeOuterParentheses(self, s):
        result = ""
        ind = 1
        brac_count = 1
        while ind < len(s):
            if s[ind] == "(":
                brac_count += 1
            else:
                brac_count -= 1
            if brac_count == 0:
                ind += 2
                brac_count = 1
            else:
                result += s[ind]
                ind += 1  
    
        return result             
