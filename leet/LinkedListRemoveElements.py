class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def list_print(head):
    if not head:
        print(head)
    curr = head
    while curr is not None:
        print(curr.val, end=' ')
        curr = curr.next
    print()


def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    while head and head.val == val:
        head = head.next
    curr = prev = head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    list_print(head)
    head = removeElements(head, 2)
    list_print(head)