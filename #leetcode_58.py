class Solution:
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        count = 0
        while i >= 0 and s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1
        return count
        