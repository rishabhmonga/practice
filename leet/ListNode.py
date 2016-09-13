class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def printList(start):
        while start is not None:
            print(start.val)
            start = start.next
        print("\n")

# inputNode = ListNode(1)
# inputNode.next = ListNode(2)
# inputNode.next.next = ListNode(3)
# inputNode.next.next.next = ListNode(4)
# ListNode.printList(inputNode)
