# 19. Remove Nth Node from End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        current = self.recur(head)
        temp = current
        if n == 1:  
            dup = temp
            if temp.next == None:
                return None
            temp = temp.next
            dup.next = None
        s = temp    
        for i in range(1,n):
            if i + 1 == n :
                temp.next = temp.next.next
                break
            temp = temp.next 
        
        curr = self.recur(s)
        return curr

    def recur(self, head):
        prev    = None
        current = head
        nex     = head.next
        while nex != None:
            current.next = prev
            prev = current
            current = nex
            nex = nex.next 
        current.next = prev
        return current