class QueueSuingStacks:
    def __init__(self):
        self.main_stack = []
        self.aux_stack = []

    def push(self, x):
        for i in range(len(self.main_stack)):
            self.aux_stack.append(self.main_stack.pop())
        self.aux_stack.append(x)
        for i in range(len(self.aux_stack)):
            self.main_stack.append(self.aux_stack.pop())
        print("Aux : ", self.aux_stack)
        print("Main : ", self.main_stack)

    def pop(self):
        return self.main_stack.pop()

    def peek(self):
        return self.main_stack[-1] if len(self.main_stack) != 0 else None

    def empty(self):
        return True if len(self.main_stack) == 0 else False

if __name__ == '__main__':
    queue = QueueSuingStacks()
    queue.push(1)
    queue.push(2)
    print(queue.peek())
