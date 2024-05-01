# 2000. Reverse Prefix of Word

class Solution:
    def reversePrefix(self, word, ch):
        i = 0
        while i < len(word) and ch != word[i]:
            i += 1
        if i != len(word):    
            prefix = word[0 : i + 1][::-1]    
            suffix = word[i + 1 :]
            word = prefix + suffix
        return word    