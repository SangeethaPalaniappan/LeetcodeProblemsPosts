# 2181. Merge Nodes in Between Zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head):
        temp = head.next
        val = 0
        dup = ListNode()
        temp_dup = dup
        while temp != None:
            while temp.val != 0:
                val += temp.val
                temp = temp.next
            temp_dup.next = ListNode(val)
            temp = temp.next
            temp_dup = temp_dup.next
            val = 0
        return dup.next
