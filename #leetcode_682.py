# 682. Baseball Game

class Solution:
    def calPoints(self, operations):
        arr = []
        i = 0
        while i < len(operations):
            if operations[i] == "D":
                length = len(arr) - 1 
                arr.append(int(arr[length]) * 2)
            elif operations[i] == "C":    
                arr.pop()
            elif operations[i] == "+":
                length = len(arr) - 1
                arr.append(int(arr[length]) + int(arr[length - 1]))
            else:
                arr.append(int(operations[i]))
            i += 1

        sums = 0
        for i in arr:
            sums += i
        return sums


