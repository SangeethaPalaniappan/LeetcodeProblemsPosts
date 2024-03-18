# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        Prev = None
        Center = head
        if head == None:
            return head
        Next = head.next 
            
        while Next != None:
            Center.next = Prev
            Prev = Center
            Center = Next
            Next = Center.next 
            
        Center.next = Prev
        head = Center
        
        return head   

                 



