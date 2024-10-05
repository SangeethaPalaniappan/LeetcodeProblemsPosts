# 2390. Removing Stars From a String 

class Solution:
    def removeStars(self, s)r:
        stack = []
        pointer = 0
        while pointer < len(s):
            if len(stack) == 0:
                stack.append(s[pointer])
            elif s[pointer] == "*":
                stack.pop()
            else:
                stack.append(s[pointer])
            pointer += 1
        res_string = ""
        for i in stack:
            res_string += i
        return res_string
