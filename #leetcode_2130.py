# 2130. Maximum Twin Sum of a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head):
        slow = head
        fast = head
        maxi = 0
        while fast != None:
            slow = slow.next
            fast = fast.next.next
        sec_part = self.reverse(slow)

        while sec_part != None:
            print(head.val, sec_part.val)
            tot = head.val + sec_part.val
            if tot > maxi:
                maxi = tot
            sec_part = sec_part.next
            head = head.next
            
        return maxi

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
