class StackNode:
    def __init__(self, val=0):
        self.val = val
        self.nextNode = None
        self.prevNode = None


class MyStack:
    topNode = None

    def top(self):
        return self.topNode

    def __init__(self, val=0):
        self.topNode = StackNode(val)

    def push(self, num):
        if self.topNode:
            tempNode = StackNode(num)
            self.topNode.nextNode = tempNode
            tempNode.prevNode = self.topNode
            self.topNode = tempNode
        else:
            self.topNode = StackNode(num)
        return self.topNode

    def pop(self):
        curr = None
        if self.topNode:
            curr = self.topNode
            self.topNode = self.topNode.prevNode
            if self.topNode:
                self.topNode.nextNode = None
        return curr


if __name__ == '__main__':
    myStack = MyStack(5)

    print(myStack.top().val)
    myStack.push(4)
    myStack.push(3)
    myStack.push(2)
    myStack.push(1)

    print(myStack.pop().val)
    print(myStack.pop().val)
    print(myStack.pop().val)
    print(myStack.pop().val)
    print(myStack.pop().val)

    print(myStack.push(10).val)
