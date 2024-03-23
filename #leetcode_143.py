# 143. Reorder List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None or head.next.next == None:
            return head
        slow = head 
        fast = head
        temp = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        sec_half = slow.next
        slow.next = None

        sec_half = self.reverseList(sec_half)


        while temp.next != None:
            temp_next = temp.next
            temp.next = sec_half
            sec_half = sec_half.next
            temp.next.next = temp_next
            temp = temp_next

        if sec_half != None:
            temp.next = sec_half

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
