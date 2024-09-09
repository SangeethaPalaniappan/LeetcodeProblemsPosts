# 520. Detect Capital

class Solution:
    def detectCapitalUse(self, word):
        cap = 0
        change = 0
        enter = 0
        for i in range(len(word)):
            if ord(word[i]) >= 65 and ord(word[i]) <= 90:
                enter = 1
                if i == 0:
                    cap += 1
                    change = 1
                if i != 0 and change == 1:
                    cap += 1        

        if cap == 0 and change == 0 and enter == 0:
            return 1

        if cap == 1 and change == 1:
            return 1
        if cap == len(word) and change == 1:
            return 1
        return 0    
