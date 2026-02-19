class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        self.stack1.append(x)


    def pop(self):

        while(self.stack1):
            self.stack2.append(self.stack1.pop())
        popped = self.stack2.pop()
        
        while(self.stack2):
            self.stack1.append(self.stack2.pop())

        self.display()
        return popped

        """
        :rtype: int
        """
        

    def peek(self):
        if self.stack1:
            return self.stack1[0]
        elif self.stack2:
            return self.stack2[0]
        

    def empty(self):
        if self.stack1 or self.stack2:
            return False
        else:
            return True
    
    def display(self):
        print(self.stack1)


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.display()
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)