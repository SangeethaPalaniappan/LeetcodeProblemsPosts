# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s):
        start_ind = 0
        end_ind = len(s) - 1
        lis = list(s)
        while start_ind < end_ind:
            while lis[start_ind].lower() != "a" and lis[start_ind].lower() != "e" and lis[start_ind].lower() != "i" and lis[start_ind].lower() != "o" and lis[start_ind].lower() != "u" and start_ind < end_ind:
                start_ind += 1
            while lis[end_ind].lower() != "a" and lis[end_ind].lower() != "e" and lis[end_ind].lower() != "i" and lis[end_ind].lower() != "o" and lis[end_ind].lower() != "u" and start_ind < end_ind:
                end_ind -= 1
            lis[start_ind], lis[end_ind] = lis[end_ind], lis[start_ind]
            start_ind += 1
            end_ind -= 1
        emp_str = ""
        for num in lis:
            emp_str += num
        return emp_str    
