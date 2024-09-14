# 3174. Clear Digits

class Solution:
    def clearDigits(self, s):
        stack = []
        i = 0
        while i < len(s):
            if ord(s[i]) >= 97 and ord(s[i]) <= 122:
                stack.append(s[i])
            else:
                if len(stack) != 0:
                    stack.pop()    
            i += 1
        res = ""
        for k in stack:
            res += k
        return res            
