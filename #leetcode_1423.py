# 1423. Maximum Points You Can Obtain from Cards

class Solution:
    def maxScore(self, cardPoints, k):
        tot = sum(cardPoints[0:k])
        maxi = tot
        n = k - 1
        end = len(cardPoints) - 1
        while n >= 0:
            tot -= cardPoints[n]
            tot += cardPoints[end]
            end -= 1
            n -= 1
            maxi = max(tot, maxi)
        return maxi    
