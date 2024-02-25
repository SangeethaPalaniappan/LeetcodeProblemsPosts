# 383. Ranson Note

class Solution:
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return 0
        d = {}
        for i in range(len(magazine)):
            if magazine[i] not in d.keys():
                d[magazine[i]] = 1
            else:
                d[magazine[i]] += 1

        d_1 = {}
        for i in ransomNote:
            if i not in d_1.keys():
                d_1[i] = 1
            else:
                d_1[i] += 1
                
        for j in ransomNote:
            if j in d.keys():
                if d_1[j] <= d[j]:
                    continue
                else:
                    return 0    
            else:
                return 0

        return 1            