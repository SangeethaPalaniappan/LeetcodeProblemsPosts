# 445. Add Two Numbers II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        list1 = self.reverse(l1)
        list2 = self.reverse(l2)
        result = self.addTwoNumbersI(list1, list2)
        return self.reverse(result)


    
    def reverse(self, ll):
        prev = None
        current = ll
        nex = current.next
        while nex != None:
            current.next = prev
            prev = current
            current = nex
            nex = nex.next
        current.next = prev
        ll = current

        return ll
    
    def addTwoNumbersI(self, l1, l2):
        temp1 = l1
        temp2 = l2
        while temp1 != None and temp2 != None:
            val = temp1.val + temp2.val
            if val > 9:
                val = val % 10
                if temp1.next != None:
                    temp1.next.val += 1
                elif temp2.next != None:
                    temp2.next.val += 1
                    temp1.next = temp2.next
                    temp1.val = val
                    temp1 = temp1.next
                    break
                else:
                    temp1.val = val
                    temp1.next = ListNode(1)

            if temp1.next == None and temp2.next != None:
                temp1.val = val
                temp1.next = temp2.next   
                temp1 = temp1.next
                break
            temp1.val = val
            temp1 = temp1.next
            temp2 = temp2.next
    

        while temp1 != None:
            if temp1.val > 9:
                temp1.val = temp1.val % 10
                if temp1.next != None:
                    temp1.next.val += 1   
                elif temp1.next == None:
                    temp1.next = ListNode(1)    
            else:
                break        
            temp1 = temp1.next
        return l1    
