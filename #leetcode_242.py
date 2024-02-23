class Solution:
    def isAnagram(self, s, t):
        if len(s) > len(t) or len(t) > len(s):
            return 0
        has = {}
        for i in s:
            if i not in has:
                has[i] = 1
            else:
                has[i] += 1  
        hash_ = {}           
        for j in t:
            if j not in hash_:
                hash_[j] = 1
            else:
                hash_[j] += 1     
        for k in s:
            if k in has.keys() and k in hash_.keys():
                if has[k] != hash_[k]:
                    return 0
            else:
                return 0        
        return 1