# 1171. Remove Zero Sum Consecutive Nodes from Linked List 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head):
        temp = head
        move = head
        change = head
        while temp != None:
            move = temp
            tot =  0
            while move != None:
                tot += move.val
                if tot == 0:
                    if temp == head:
                        if move.next == None:
                           temp = None
                           head = None
                           move = None
                        else:      
                           head = move.next 
                           temp = move.next 
                    elif temp != head:
                        change.next = move.next
                        temp = head
                    elif move.next == None:
                        change.next = None 
                    break      
  
             
                move = move.next
            else:
               change = temp   
               temp = temp.next     
  
        return head        
