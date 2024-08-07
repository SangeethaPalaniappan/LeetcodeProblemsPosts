# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        count = 0
        hashmap = {}
        i = 0
        j = i
        maxi = 0
        while j < len(s):
            if s[j] in hashmap and  hashmap[s[j]] >= i:
                i = hashmap[s[j]] + 1
            hashmap[s[j]] = j    
            count = j - i + 1
            maxi = max(count, maxi)
            j += 1           
        return maxi                  
