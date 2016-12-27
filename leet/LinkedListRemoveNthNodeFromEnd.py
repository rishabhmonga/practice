class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    start = ListNode(0)
    slow = start
    fast = start
    slow.next = head

    for i in range(n+1):
        fast = fast.next

    while fast is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return start.next


def list_print(head):
    curr = head
    while curr is not None:
        print(curr.val, end=' ')
        curr = curr.next
    print()


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    list_print(head)
    head = removeNthFromEnd(head, 1)
    list_print(head)
