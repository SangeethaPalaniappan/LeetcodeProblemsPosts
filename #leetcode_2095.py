# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):  

        if head.next == None:
            return head.next
        
        slow, fast, slow_prev = head, head, head  
        
        while fast != None and fast.next != None:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next
            
        slow_prev.next = slow.next
        return head
