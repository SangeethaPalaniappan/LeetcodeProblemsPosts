# 2678. Number of Senior Citizens

class Solution:
    def countSeniors(self, details):
        count = 0
        for det in details:
            age = det[11:13]
            if int(age) > 60:
                count += 1
        return count        
