# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return digits
        s = digits
        m = s[:]
        dic = {"2" :"abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        arr = []
        string = ""
        self.func(s, dic, m, arr, string, 0)
        return arr
                  

    def func(self, val_str, dic, gn_str, arr, string, ind):
        if len(gn_str) == len(string):
            arr.append(string)
            return
        
        curr_char = val_str[ind]
        for i in dic[curr_char]:
            self.func(val_str, dic, gn_str, arr, string + i, ind + 1)
                
  
