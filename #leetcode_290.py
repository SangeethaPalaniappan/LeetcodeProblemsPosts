# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern, s):
        s = list(s.split(" "))
        if len(s) != len(pattern):
            return 0
        else:
            hashmap = {}
            hm_1 = {}
            for i in range(len(s)):
                if pattern[i] not in hashmap:
                    hashmap[pattern[i]] = s[i]
                else:
                    if hashmap[pattern[i]] == s[i]:
                        continue
                    else:
                        return 0       
                if s[i] not in hm_1:
                    hm_1[s[i]] = pattern[i]
                else:
                    if hm_1[s[i]] == pattern[i]:
                        continue
                    else:
                        return 0                     
            return 1
