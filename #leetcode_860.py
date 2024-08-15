# 860. Lemonade Change

class Solution:
    def lemonadeChange(self, bills):
        hashmap = {5 : 0, 10 : 0, 20 : 0}
        for i in range(len(bills)):
            if bills[i] == 5:
                hashmap[5] += 1
            elif bills[i] == 10:
                hashmap[10] += 1
                if hashmap[5] > 0:
                    hashmap[5] -= 1
                else:
                    return 0
            elif bills[i] == 20:
                if hashmap[10] > 0:
                    hashmap[10] -= 1
                    if hashmap[5]  > 0:
                        hashmap[5] -= 1
                    else:
                        return 0    
                elif hashmap[5] > 2:    
                    hashmap[5] -= 3
                else:
                    return 0
     
        return 1                
