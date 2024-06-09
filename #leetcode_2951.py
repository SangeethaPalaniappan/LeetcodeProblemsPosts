# 2951. Find the Peaks

class Solution:
    def findPeaks(self, mountain):
        index_arr = []
        index = 1
        length = len(mountain) - 1    
        while index < length:    
            if mountain[index] > mountain[index - 1] and mountain[index] > mountain[index + 1]:
                index_arr.append(index)
                index += 2
            else:
                index += 1
        return index_arr        