# 76. Minimum Window Substring

class Solution:
    def minWindow(self, s, t) :
        mini = float("inf")
        hashset = {}
        for k in t:
            if k not in hashset:
                hashset[k] = 1
            else:
                hashset[k] += 1
        word = ""         
        right, left, change, length = 0, 0, 0, 0
        hashmap = {}    

        leng = len(s)
        len_t = len(t)
        while right < leng:

            if change == 0 and s[right] not in hashset:
                if right == left:
                    left += 1
                right += 1
                continue
            change = 1   
            if s[right] in hashset:
                if s[right] not in hashmap:    
                    hashmap[s[right]] = 1
                else:
                    hashmap[s[right]] += 1
                if hashmap[s[right]] <= hashset[s[right]]:
                    length += 1

            right += 1
            if length == len_t:
                count = (right - left) + 1
                if mini > count:
                    mini = count
                    word = s[left : right]
                    
                while length == len_t:
                    if s[left] not in hashset:
                        left += 1 
                        count = (right - left) + 1
                               
                    else:
                        if hashmap[s[left]] == hashset[s[left]]:
                            length -= 1
                          
                        count = (right - left) + 1
                        if mini > count:
                            mini = count
                            word = s[left : right]
                                 
                        hashmap[s[left]] -= 1
                        
                        left += 1     
                change = 0       

                
        return word
