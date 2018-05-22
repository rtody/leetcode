# Implement stack using queue version 1 - use two queues

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
        # print('Push', x)
        self.stack.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        tmp_stack = Queue()
        while (True):
            top = self.stack.get()

            # Not the top one we want, keep looping
            if not self.stack.empty():
                tmp_stack.put(top)
            else:
                # Copy the temporary queue to main queue
                for i in tmp_stack.queue:
                    self.stack.put(i)
                # print('Pop', top)
                return top

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        tmp_stack = Queue()
        while (True):
            top = self.stack.get()
            tmp_stack.put(top)
            # empty stack means we get to the top one
            if self.stack.empty():
                for i in tmp_stack.queue:
                    self.stack.put(i)
                # print('Top', top)
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
