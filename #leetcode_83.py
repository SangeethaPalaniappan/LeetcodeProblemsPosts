# 83. Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return head

        temp = head
        dup = temp.next
        while dup != None:
            if temp.val == dup.val:
                dup = dup.next
                
            else:
                temp.next = dup
                temp = dup
                dup = dup.next
        
        return head            