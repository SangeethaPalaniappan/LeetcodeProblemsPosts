# 1290. Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:
        temp = self.reverse(head)
        integer = 0
        index = 0
        while temp != None:
            integer += ((2 ** index) * temp.val)
            temp = temp.next
            index += 1
        return integer

    def reverse(self, head):
        prev = None
        curr = head
        then = head.next
        while then != None:
            curr.next = prev
            prev = curr
            curr = then
            then = then.next
        curr.next = prev
        return curr        
