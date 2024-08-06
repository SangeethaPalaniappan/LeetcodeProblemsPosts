# 3016. Minimum Number of Pushes to Type Word II

class Solution:
    def minimumPushes(self, word):
        tot_char = set(word)
        if len(tot_char) <= 8:
            return len(word)
        else:
            hashmap = {}
            for i in range(len(word)):
                if word[i] not in hashmap:
                    hashmap[word[i]] = 1
                else:
                    hashmap[word[i]] += 1
            val = list(hashmap.values())         
            val = sorted(val, reverse=True)

            start = 0
            end = 8
            tot = 0
            place = 1
            
            while end < len(val):
                lis = val[start:end]
                for i in lis:
                    tot += (i * place)
                start = end
                end += 8
                place += 1

            lis = val[start:]  
            if len(lis) > 0:
                for i in lis:
                    tot += (i * place)

            return tot 
