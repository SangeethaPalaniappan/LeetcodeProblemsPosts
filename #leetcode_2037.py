# 2037. Minimum Number of Moves to Seat Everyone

class Solution:
    def minMovesToSeat(self, seats, students):
        result = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            result += (abs(seats[i] - students[i]))
        return result    