# 3042. Count Prefix and Suffix Pairs I

class Solution:
    def countPrefixSuffixPairs(self, words):
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.check(words[i], words[j]) == 1:
                    count += 1
        return count            
                
        
    def check(self, str_1, str_2):
        length = len(str_1)
        count = 0         
        if str_2[0 : length] == str_1 and str_2[(len(str_2) - length): len(str_2)] == str_1:
            count = 1
        return count        
                    
