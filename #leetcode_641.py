# 641. Design Circular Deque

from collections import deque
class MyCircularDeque:

    def __init__(self, k):
        self.size = k
        self.queue = deque([])

    def insertFront(self, value):
        if self.size == len(self.queue):
            return 0
        self.queue.appendleft(value)
        return 1

    def insertLast(self, value):
        if self.size == len(self.queue):
            return 0
        self.queue.append(value)
        return 1

    def deleteFront(self):
        if 0 == len(self.queue):
            return 0
        self.queue.popleft()
        return 1

    def deleteLast(self):
        if 0 == len(self.queue):
            return 0
        self.queue.pop()
        return 1

    def getFront(self)t:
        if 0 == len(self.queue):
            return -1
        ans = self.queue[0]
        return ans

    def getRear(self):
        if 0 == len(self.queue):
            return -1
        ans = self.queue[-1]
        return ans

    def isEmpty(self):
        if len(self.queue) == 0:
            return 1
        return 0

    def isFull(self):
        if len(self.queue) == self.size:
            return 1
        return 0


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
