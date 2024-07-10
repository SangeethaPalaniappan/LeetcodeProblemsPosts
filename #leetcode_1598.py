# 1598. Crawler Log Folder

class Solution:
    def minOperations(self, logs):
        stack = []
        count = 0
        for i in logs:
            if i == "../" and len(stack) != 0:
                val = stack.pop()
                count -= 1
            else:
                if i != "./" and i != "../":
                    stack.append(i)
                    count += 1

        return count        
