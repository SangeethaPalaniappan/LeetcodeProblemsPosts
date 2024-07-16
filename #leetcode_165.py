# 165. Compare Version Numbers

class Solution:
    def compareVersion(self, version1, version2):
        l1 = version1
        l2 = version2
        i, j = 0, 0
        while i < len(l1) or j < len(l2):
            n1 = 0
            n2 = 0
            while i < len(l1) and l1[i] != ".":
                n1 = (n1 * 10) + int(l1[i])
                i += 1

            while j < len(l2) and l2[j] != ".":
                n2 = (n2 * 10) + int(l2[j])
                j += 1

            if n1 > n2:
                return 1
            if n1 < n2:
                return -1    
      
            i += 1
            j += 1
            print(i,j)
        return 0   

