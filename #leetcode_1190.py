# 1190. Reverse Substrings Between Each Pair of Parentheses

class Solution:
    def reverseParentheses(self, s):
        if len(s) < 3:
            return s
        stack = []
        for i in range(len(s)):
            if s[i] == ")":
                start = i
                string = ""
                while stack[-1] != "(":
                    val = stack.pop()
                    string += val
                stack.pop()    
                for k in string:
                    stack.append(k)            

            else:
                stack.append(s[i])
     
        fin_str = ""        
        while len(stack) != 0:
            val = stack.pop()
            fin_str += val   

        return fin_str[::-1]    
                  
