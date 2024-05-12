# 171. Excel Sheet Column Number

class Solution:
    def titleToNumber(self, columnTitle):
        start = 0
        end = len(columnTitle) - 1
        
        x = 0
        dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
        column_no = 0
        while start <= end:
            column_no = column_no + (dic[columnTitle[end]] * (26 ** x))
            end -= 1
            x += 1
        return column_no    