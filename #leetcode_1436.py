#1436. Destination City

class Solution:
    def destCity(self, paths):
        dict = {}
        for i in range(len(paths)):
            if paths[i][0] not in dict.keys():
                dict[paths[i][0]] = 1
            else:
                dict[paths[i][0]] += 1    
            if paths[i][1] not in dict.keys():
                dict[paths[i][1]] = 1
            else:
                dict[paths[i][1]] += 1    
        arr = []
        for j in range(len(paths)):
            if dict[paths[j][1]] == 1:
                return paths[j][1]       