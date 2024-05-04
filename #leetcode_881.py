# 881. Boats to Save People

class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        print(people)
        i = 0
        j = len(people) - 1
        boat_count = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            elif people[j] <= limit:
                j -= 1
            elif i == j:
                j -= 1    
            boat_count += 1

        return boat_count    