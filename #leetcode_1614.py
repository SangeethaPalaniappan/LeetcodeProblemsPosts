# 1614. Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s):
        count = 0
        maxi = 0 
        for i in s:
            if i == ")":
                count -= 1
            elif i == "(":
                count += 1 
                if count > maxi:
                    maxi = count
        return maxi     
