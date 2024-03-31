# 20. valid Parentheses

class Solution:
    def isValid(self, s):
        if len(s) % 2 != 0:
            return 0
        arr = []
        p = 0
        for brackets in range(len(s)):
            if s[brackets] == "(" or s[brackets] == "[" or s[brackets] == "{":
                arr.append(s[brackets])
                
            else:    
                if len(arr) != 0:
                    if s[brackets] == "]":
                        if arr[len(arr) - 1] == "[":
                            arr.pop()
                        else:
                            return 0
                    elif s[brackets] == "}":
                        if arr[len(arr) - 1] == "{":
                            arr.pop()
                        else:
                            return 0        
                    elif s[brackets] == ")":
                        if arr[len(arr) - 1] == "(":
                            arr.pop()
                        else:
                            return 0
               
                elif len(arr) == 0:
                    return 0       
     
        if len(arr) == 0:
            return 1                 
                               
