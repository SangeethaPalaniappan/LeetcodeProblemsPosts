# 1684. Count the Number of Consistent Strings

class Solution:
    def countConsistentStrings(self, allowed, words):
        hashset = set()
        count = 0
        for i in allowed:
            if i not in hashset:
                hashset.add(i)
        for word in words:
            for char in word:
                if char not in hashset:
                    break
            else:
                count += 1 
        return count               
