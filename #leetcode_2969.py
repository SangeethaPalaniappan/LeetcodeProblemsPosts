# 2969. Minimum String Length After Removing Substrings

class Solution:
    def minLength(self, s):
        stack = []
        pointer = 0
        while pointer < len(s):
            if len(stack) == 0:
                stack.append(s[pointer])
            elif s[pointer] == "B" and stack[-1] == "A":
                stack.pop()
            elif s[pointer] == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(s[pointer])
            pointer += 1
        return len(stack)
                
