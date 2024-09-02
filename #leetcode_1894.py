# 1894. Find the Student that Will Replace the Chalk

class Solution:
    def chalkReplacer(self, chalk, k):
        val = 0
        i = 0
        tot = sum(chalk)
        k = k % tot
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            else:
                k -= chalk[i]
             

            
        return i      
