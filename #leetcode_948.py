# 948. Bag of Tokens

class Solution:
    def bagOfTokensScore(self, tokens, power):
        if len(tokens) == 0:
            return 0
        tokens.sort()
        i = 0
        j = len(tokens) - 1
        count = 0
        maxi = 0
        ite = 0
        while i <= j:
            if tokens[i] <= power:
                power -= tokens[i]
                count += 1
                i += 1
                ite += 1
            elif count >= 1:
                power += tokens[j] 
                count -= 1
                j -= 1
                ite += 1
            maxi = max(maxi, count)    
             
            if ite == 0 and count == 0:
                return maxi
                break
        return maxi       