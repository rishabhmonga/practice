import sys


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_list = []
        self.min = -sys.maxsize
        self.min_idx = -sys.maxsize

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack_list) == 0 or self.min > x:
            self.min = x
            self.stack_list.append(x)
            self.min_idx = len(self.stack_list) - 1
        else:
            temp = self.stack_list.pop()
            self.stack_list.append(x)
            self.stack_list.append(temp)

    def pop(self):
        """
        :rtype: void
        """
        if self.min_idx == len(self.stack_list) - 1:
            self.stack_list.pop()
            self.find_min()
        else:
            temp = self.stack_list.pop()
            self.stack_list.pop()
            self.stack_list.append(temp)

    def top(self):
        """
        :rtype: int
        """
        if self.min_idx == len(self.stack_list) - 1:
            return self.stack_list[-1]
        else:
            return self.stack_list[-2]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack_list[-1]

    def find_min(self):
        """
        :rtype: void
        """
        if len(self.stack_list) > 0:
            self.min = -sys.maxsize
            for i in range(len(self.stack_list)):
                if self.stack_list[i] < self.min:
                    self.min = self.stack_list[i]
                    self.min_idx = i


if __name__ == '__main__':
    obj = MinStack()
    obj.push(3)
    print(obj.getMin())
    obj.push(2)
    print(obj.getMin())
    obj.push(1)
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())

    # param_3 = obj.top()
    # param_4 = obj.getMin()
