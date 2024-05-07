# 2816. Double a Number Represented as a Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head):
        if head.val == 0:
            return head
        integer = 0
        temp = head
        while temp != None:
            integer = integer * 10 + temp.val
            temp = temp.next
      
        double = integer * 2
        temp = head
        linked_list = None
        while double != 0:
            rem = double % 10
            double //= 10
            node = ListNode(rem)
            node.next = linked_list
            linked_list = node
        return  linked_list 
        