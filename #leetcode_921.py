# 921. Minimum Add to Make Parentheses Valid

class Solution:
    def minAddToMakeValid(self, s):
        stack = []
        pointer = 0
        while pointer < len(s):
            if len(stack) == 0:
                stack.append(s[pointer])
            elif stack[-1] == "(" and s[pointer] == ")":
                stack.pop()
            else:
                stack.append(s[pointer])
            pointer += 1
        return len(stack)
