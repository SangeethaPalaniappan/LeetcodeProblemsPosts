# 24. Swap Nodes in Pairs

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        dummy = ListNode()
        dummy.next = head
        temp = head
        then = temp.next
        head = then
        prev = dummy
        while then != None and then.next != None:
            temp.next = then.next
            then.next = temp
            prev.next = then
            prev = temp
            temp = temp.next
            then = temp.next
        if then != None:    
            temp.next = then.next
            then.next = temp
            prev.next = then
        return dummy.next
