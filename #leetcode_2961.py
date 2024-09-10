# 2961. Double Modular Exponentiation

class Solution:
    def getGoodIndices(self, variables, target):
        good_indices_array = []
        
        for i in range(len(variables)):
            integer = (((variables[i][0] ** variables[i][1]) % 10) ** variables[i][2] ) % variables[i][3]
            if integer == target:
                good_indices_array.append(i)
        return good_indices_array        
