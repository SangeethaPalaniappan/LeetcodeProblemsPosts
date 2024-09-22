# 23. Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None

        arr = []

        for i in range(len(lists)):
            node = lists[i]
            while node != None:
                arr.append(node.val)
                node = node.next
  
        arr.sort()  
        if len(arr) != 0: 
            return self.linkedlist(arr)
            return None

    def linkedlist(self, arr):
        
        head = ListNode(arr[0])
        temp = head
        for i in range(1, len(arr)):
            new_node = ListNode(arr[i])
            temp.next = new_node
            temp = temp.next
        return head    


