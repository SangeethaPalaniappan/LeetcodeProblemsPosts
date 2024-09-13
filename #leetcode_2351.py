# 2351. First Letter to Appear Twice

class Solution:
    def repeatedCharacter(self, s):
        hashmap = {}
        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
                if hashmap[i] == 2:
                    return i
                        
