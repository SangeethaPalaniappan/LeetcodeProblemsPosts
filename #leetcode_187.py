# 187. Repeated DNA Sequences

class Solution:
    def findRepeatedDnaSequences(self, s): 
        hashset = set()
        an_hs = set()
        start = 0
        end = 10
        while end <= len(s):
            word = s[start:end]
            if word not in hashset:
                hashset.add(word)
            else:
                an_hs.add(word)
            start += 1
            end += 1
        return list(an_hs)
