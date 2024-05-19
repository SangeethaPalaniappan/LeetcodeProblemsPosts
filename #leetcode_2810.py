# 2810. Faulty Keyboard

class Solution:
    def finalString(self, s):
        if len(s) == 1:
            return s
        emp_str = ""
        for i in s:
            if i == "i":
                emp_str = self.reverse(emp_str)
            else:
                emp_str += i 
        fin_str = ""
        for char in emp_str:
            fin_str += char        
        return fin_str        

    def reverse(self, string):
        start = 0
        end = len(string) - 1
        string = list(string)
        while start < end:
            string[start], string[end] = string[end], string[start]               
            start += 1
            end -= 1
        return string    
    