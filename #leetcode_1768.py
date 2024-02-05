class Solution:
    def mergeAlternately(self, word1, word2):
        mini = min(len(word1), len(word2))
        d = ""
        for i in range(mini):
            d += word1[i] + word2[i]
        return d + word1[mini:] + word2[mini:]