# 2085. Count Common Words With One Occurrence

class Solution:
    def countWords(self, words1, words2):
        dic = {}

        count = 0
        for words in words1:
            if words not in dic:
                dic[words] = 1
            else:
                dic[words] += 1
       # print("w1:", dic)      

        for words in words2:
            if words in dic:
                if dic[words] == 1:
                    dic[words] -= 1
                elif dic[words] == 0:
                    dic[words] = 1    
        # print("w2:", dic_1)

        for i in dic.keys():
            if dic[i] == 0:
                count += 1


        return count