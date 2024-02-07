# 451. Sort Characters By Frequency
 
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1    
        emp_str = ""
        sorted_value_index = sorted(dic, key=dic.get, reverse=True)
        
        for key in sorted_value_index:
            emp_str += (key * dic[key])
  
        return emp_str