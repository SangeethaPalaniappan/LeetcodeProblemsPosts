# 1346. Check If N and Its Doube Exist

class Solution:
    def checkIfExist(self, arr):
        sets = set()
        for i in arr:
            if len(sets) == 0:
                sets.add(i)
                
            else:
                
                if i % 2 == 0:
                    half = i // 2
                    if half in sets:
                        return 1
                double = 2 * i        
                if double in sets:
                    return 1
                else:
                    sets.add(i)        
        return 0            