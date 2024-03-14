#1436. Destination City

class Solution:
    def destCity(self, paths):
        dic = {}
        for i in range(len(paths)):
            if paths[i][0] not in dic:
                dic[paths[i][0]] = 0
            else:
                dic[paths[i][0]] = -1     
            if paths[i][1] not in dic:
                dic[paths[i][1]] = 1   
            else:
                dic[paths[i][1]] = -1           
        for key in dic:
            if dic[key] == 1:
                return key      