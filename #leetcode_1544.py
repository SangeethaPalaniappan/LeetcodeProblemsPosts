# 1544. Make The String Great

class Solution:
    def makeGood(self, s):
        if len(s) == 1:
            return s
        stack = []
        n = len(s)
        for i in range(n):   
            if len(stack) != 0:
                diff = ord(stack[-1]) - ord(s[i])
                if abs(diff) == 32:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        string = ""
        for j in stack:
            string += j                
        return string            
            