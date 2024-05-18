# 709. To Lower Case

class Solution:
    def toLowerCase(self, s):
        fin_str = ""
        for i in s:
            if ord(i) >= 65 and ord(i) <= 90:
                i = chr(ord(i) + 32)
            fin_str += i

        return fin_str        