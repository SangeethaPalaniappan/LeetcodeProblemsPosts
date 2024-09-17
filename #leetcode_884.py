# 884. Uncommon Words from Two Sentences

class Solution:
    def uncommonFromSentences(self, s1, s2):
        res = []
        lis1 = list(s1.split())
        lis2 = list(s2.split())
        h1 = {}
        for i in lis1:
            if i not in h1:
                h1[i] = 1
            else:
                h1[i] += 1
        for k in lis2:
            if k not in h1:
                h1[k] = 1
            else:
                h1[k] += 1       
        for j in h1:
            if h1[j] == 1:
                res.append(j)
        return res        
