# Implement stack using queue version 2 - use one queue

from queue import Queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        print('Push', x)
        self.stack.put(x)
        stack_sz = self.stack.qsize()

        while (stack_sz > 1):
            self.stack.put(self.stack.get())
            stack_sz = stack_sz - 1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        top = self.stack.get()
        print('Pop', top)
        return top

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        top = self.stack.queue[0]
        print('Top', top)
        return top

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        """
        if self.stack.empty():
            print('Empty')
        else:
            print('Non Empty')
        """
        return self.stack.empty()

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(5)
obj.push(4)
obj.push(3)
obj.push(2)
obj.push(1)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
