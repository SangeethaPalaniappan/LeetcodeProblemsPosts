# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s, t):
        dic   = {}
        dic_1 = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = t[i] 
                if t[i] not in dic_1:
                    dic_1[t[i]] = s[i]  
                else:
                    if dic_1[t[i]] == s[i]: 
                        continue
                    else:
                        return 0     
            else:
                if dic[s[i]] == t[i]:
                    continue
                else:
                    return 0
        return 1                        