# 394. Decode String

class Solution:
    def decodeString(self, s):
        stack = []
        fin_str = ""
        for i in s:
            if i == "]":
                string = ""
                while stack[-1] != "[":
                    val = stack.pop()
                    string = val + string
                stack.pop()
                times = stack.pop()
                while len(stack) != 0 and ord(stack[-1]) >= 47 and ord(stack[-1]) <= 58:
                    times = stack.pop() + times
                f = (int(times) * string)
                for l in f:
                    stack.append(l)
    
            else:
                stack.append(i)
                
        val = ""        
        while len(stack) != 0:
             val += stack.pop()    
        fin_str += val[::-1]        
        
        return fin_str          
