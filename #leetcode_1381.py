# 1381. Design a Stack With Increment Operation

class CustomStack:

    def __init__(self, maxSize):
        self.stack = []
        self.size = maxSize  

    def push(self, x):
        size = len(self.stack)       
        if self.size != len(self.stack):
           self.stack.append(x)

    def pop(self):
        if len(self.stack) != 0:    
            return self.stack.pop()
        return -1
        

    def increment(self, k, val):
        if k > len(self.stack):
            k = len(self.stack)
        if len(self.stack) != 0:   
            for i in range(k):
                if self.stack[i] != -1:
                    self.stack[i] += val




# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
