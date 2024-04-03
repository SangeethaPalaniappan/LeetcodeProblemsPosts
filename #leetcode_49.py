# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for word in strs:
            sort_word = ''.join(sorted(word))
            if sort_word not in dic:
                dic[sort_word] = []
            dic[sort_word].append(word)
        lis = list(dic.values())
        return lis