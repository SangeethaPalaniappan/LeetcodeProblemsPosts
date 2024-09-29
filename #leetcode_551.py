# 551. Student Attendance Record I

class Solution:
    def checkRecord(self, s):
        absent_count = 0
        for i in range(len(s)):
            if s[i] == "L":
                if i + 2 < len(s) and s[i + 1] == "L" and s[i + 2] == "L":
                    return 0

            elif s[i] == "A":
                absent_count += 1
                if absent_count > 1:
                    return 0
            prev = s[i]
        return 1

