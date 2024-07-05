# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next
        then = curr.next
        res = [-1, -1]
        arr = []
        ind = 1
        while then != None:
            if prev.val > curr.val and curr.val < then.val or prev.val < curr.val and curr.val > then.val:
                arr.append(ind + 1)   
            ind += 1    
            prev = curr
            curr = then
            then = then.next
        if len(arr) <= 1:
            return res
        maxi = max(arr)
        mini = min(arr)
        min_val = float('inf')
        for i in range(len(arr) - 1):
            val =  arr[i + 1] - arr[i]
            if val < min_val:
                min_val = val
        res[1] = maxi - mini
        res[0] = min_val
        return res
