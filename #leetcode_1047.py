# 1047. Remove All Adjacent Duplicates In String

class Solution:
    def removeDuplicates(self, s):
        if len(s) == 1:
            return s
        stack = []
        final_str = ""
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                continue
            
            if stack[-1] == s[i]:
                stack.pop()
            else:    
                stack.append(s[i])    

        for char in stack:
            final_str += char   
 
        return final_str                    