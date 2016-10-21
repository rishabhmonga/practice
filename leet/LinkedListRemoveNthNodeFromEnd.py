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
    curr = head
    curr_n = curr
    for i in range(n):
        curr_n = curr_n.next
    while curr_n is not None and curr_n.next is not None:
        curr = curr.next
        curr_n = curr_n.next
    curr = delete_node(curr)
    return head


def delete_node(node):
    if node.next is None:
        return None
    node.next = node.next.next
    return node


def list_print(head):
    curr = head
    while curr is not None:
        print(curr.val, end=' ')
        curr = curr.next
    print()


if __name__ == '__main__':
    head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    list_print(head)
    head = removeNthFromEnd(head, 1)
    list_print(head)
