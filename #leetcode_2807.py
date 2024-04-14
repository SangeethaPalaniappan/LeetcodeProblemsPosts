# 2807. Insert Greatest Common Divisors in Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head):
        temp = head
        while temp.next != None:
            a = temp.val
            b = temp.next.val
            gcd = self.gcd(a, b)
            gcd_node = ListNode(gcd)
            gcd_node.next = temp.next
            temp.next = gcd_node
            temp = gcd_node.next
        return head

    def gcd(self, a, b):
        maxi = 1
        mini = min(a, b)

        if a == b:
            return a
        for i in range(1, mini + 1):
            if a % i == 0 and b % i == 0:
                if maxi < i:
                    maxi = i           
        return maxi