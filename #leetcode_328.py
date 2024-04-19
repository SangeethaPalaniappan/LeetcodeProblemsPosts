# 328. Odd Even Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head)
        if head == None:
            return head
        temp_1 = head
        temp_2 = head.next
        even_head = temp_2
        
        while temp_1 != None and temp_2 != None:
            temp_1.next = temp_2.next
            if temp_1.next == None:
                temp_2.next = None
                break
            temp_1 = temp_1.next
            temp_2.next = temp_1.next
            temp_2 = temp_2.next
        temp_1.next = even_head
        return head    