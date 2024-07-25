# 139. Word Break

class Solution:
    def wordBreak(self, s, wordDict):
        return self.checking(s, wordDict, {})

    def checking(self, string, dic, hashmap):
        if string in hashmap:
            return hashmap[string]
        if string == "":
            return 1
        val = 0

        for word in dic:
            if word == string[0 : len(word)]:
                if self.checking(string[len(word) : len(string)], dic, hashmap) == 1:
                    val = 1
                    hashmap[string[0 : len(word)]] = 1
                    return val
        hashmap[string] = val   
        return val            
               
