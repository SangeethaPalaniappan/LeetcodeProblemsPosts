# 791. Custom Sort String

class Solution:
    def customSortString(self, order, s):
        new_str = ""
        dic = {}
        dic_1 = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1    
        for j in order:
            if j in dic.keys():
                count = j
                if dic[j] > 1:
                    str_ing = ""
                    count = str_ing + (j * dic[j])
                new_str += count
                dic_1[j] = 1

        for k in s:
            if k not in dic_1:
                new_str += k        
        return new_str 