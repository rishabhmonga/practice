from leet import ListNode


def getIdx(head, k):
    curr = head
    idx = 0
    while curr is not None:
        idx += 1
    return idx % k


def reverseKGroup(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    idx = getIdx(head, k)



if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    ListNode.printList(head)
    # root = reverse(head)
    # ListNode.printList(root)
