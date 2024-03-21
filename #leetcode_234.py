# 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head):
        temp = head
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        if fast != None and fast.next == None:
            slow = slow.next
        slow = self.reverseList(slow)
        while slow != None :

            if slow.val != temp.val:
                return 0
            slow = slow.next  
            temp = temp.next  
              
        return 1        
    def reverseList(self, head):
        Prev=None
        Center=head
        if head!=None:
            Next=head.next 
        else:
            return     
        while Next!=None:
            Center.next=Prev
            Prev=Center
            Center=Next
            
            Next=Next.next 
            if Next==None:
                Center.next=Prev
        head=Center
        
        return head   

        