# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s):
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1

        m = -1
        for j in dic.keys():
            if dic[j] == 1:
                m = j
                break
        for k in range(len(s)):
            if s[k] == m:
                return k      
        return m