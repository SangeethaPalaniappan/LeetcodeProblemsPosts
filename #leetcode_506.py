# 506. RelativeRanks

class Solution:
    def findRelativeRanks(self, score):
        arr = []
        for i in score:
            arr.append(i)
        score.sort(reverse = True)

        dic = {}
        for i in range(len(score)):
            if i == 0:
                dic[score[i]] = "Gold Medal"
            elif i == 1:
                dic[score[i]] = "Silver Medal"
            elif i == 2:    
                dic[score[i]] = "Bronze Medal"
            else:
                dic[score[i]] = str(i + 1)
        print(dic) 
        for j in range(len(arr)):
            arr[j] = dic[arr[j]] 
        return arr    