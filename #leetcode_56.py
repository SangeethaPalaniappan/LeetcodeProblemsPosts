# 56. Merge Interval

class Solution:
    def merge(self, intervals):
        if len(intervals) == 1:
            return intervals
        arr = []
        intervals.sort()

        i = 0
        j = i + 1
        count = 0
        end = len(intervals)
        while i < end and j < end:
            if intervals[i][1] >= intervals[j][0]:
                maxi = max(intervals[i][1], intervals[j][1])
                intervals[i][1] = maxi
                if count == 0:
                    arr.append(intervals[i])
                    count += 1
                j += 1
            else:
                if count == 0:
                    arr.append(intervals[i])
                i = j

                count = 0
    
        return arr
               

