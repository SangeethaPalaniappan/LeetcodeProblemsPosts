# 1554. Day of the Year

class Solution:
    def dayOfYear(self, date):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]
        year = int(date[:4])
        
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            month_days[1] = 29
     
        month = int(date[5 : 7])

        days = int(date[8 : 10])
        for i in range(month-1):   
            days += month_days[i]

        
        return days    