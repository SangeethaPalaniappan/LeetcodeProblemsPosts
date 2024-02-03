# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        head = l1
        temp1 = l1
        temp2 = l2

        while temp1 != None and temp2 != None:     
            s = temp1.val + temp2.val
            if s >= 10:
                m = s % 10
                if temp1.next == None:
                    temp1.next = ListNode(1)
                    
                elif temp2.next == None:
                    temp2.next = ListNode(1)
                     
                else:       
                    temp1.next.val += 1
                temp1.val = m
                
               
            else:
                temp1.val = s  
                if temp1.next == None:
                    temp1.next = temp2.next
                    return head
                elif temp2.next == None:
                    temp2.next = temp1.next 
                    return head 
                else:       
                    temp1.val = s   
            temp1 = temp1.next
            temp2 = temp2.next
        
        

        return head
        