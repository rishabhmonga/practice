from collections import deque


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_queue = deque()
        self.aux_queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.main_queue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        while len(self.main_queue) > 1:
            self.aux_queue.append(self.main_queue.popleft())
        self.main_queue.popleft()
        while len(self.aux_queue) > 0:
            self.main_queue.append(self.aux_queue.popleft())

    def top(self):
        """
        :rtype: int
        """
        return self.main_queue[-1] if not self.empty() else None

    def empty(self):
        """
        :rtype: bool
        """
        return True if len(self.main_queue) == 0 else False

if __name__ == '__main__':
    myStack = Stack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    print(myStack.empty())
    print(myStack.top())
    myStack.pop()
    myStack.pop()
    print(myStack.top())
    print(myStack.empty())
    myStack.pop()
    print(myStack.empty())
