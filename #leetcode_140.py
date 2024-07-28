# 140. Word Break II

class Solution:
    def wordBreak(self, s, wordDict):
        arr = []
        self.string_form(s, wordDict, arr, "")
        return arr

    def string_form(self, string, words, arr, fin_str):

        if string == "":
            arr.append(fin_str.strip())
            return fin_str
        val = 0    
        for word in words:
            if word == string[0 : len(word)]:
                val = self.string_form(string[len(word) : len(string)], words, arr, fin_str + " " + word)
