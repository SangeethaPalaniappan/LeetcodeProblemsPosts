# 61. Rotate List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        if k == 0 or head == None or head.next == None:
            return head
        length = 0
        temp = head
        while temp != None:
            length += 1
            last = temp
            temp = temp.next 
        if k > length:
            k = k % length     
        diff = length - k
        if k == 0 or diff == 0:
            return head
        else:
            temp = head
            for i in range(diff - 1):
                temp = temp.next

            dup = temp.next  

            temp.next = None

            last.next = head
  
            head = dup
            return head
            
