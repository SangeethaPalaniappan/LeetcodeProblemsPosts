# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 == None and list2 == None:
            return list1
        if list2 == None:
            return list1
        if list1 == None:
            return list2
                
        temp = ListNode()
        curr = temp

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next

            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
                
        if list1 == None:
            curr.next = list2
        if list2 == None:
            curr.next = list1            

        return temp.next    
