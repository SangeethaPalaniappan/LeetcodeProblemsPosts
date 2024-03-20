# 1669. Merge In Between Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        i = 0
        temp = list1
        while i < a:
            i += 1
            if i != a: 
                temp = temp.next
   
        rem_ll = temp.next

        temp.next = list2 

        while i < b:
            rem_ll = rem_ll.next
            i += 1    

        temp2 = list2   
        while temp2.next != None:
            temp2 = temp2.next 
        temp2.next = rem_ll.next  
        return list1