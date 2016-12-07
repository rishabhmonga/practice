class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    lengthA = lengthB = 0
    markerA = headA
    markerB = headB
    while headA:
        headA = headA.next
        lengthA += 1
    while headB:
        headB = headB.next
        lengthB += 1
    diff = lengthA - lengthB
    headA = markerA
    headB = markerB
    if diff > 0:
        while diff != 0:
            headA = headA.next
            diff -= 1
    else:
        while diff != 0:
            headB = headB.next
            diff += 1
    while headA is not None and headB is not None:
        if headA is headB:
            return headA
        headA = headA.next
        headB = headB.next
    return None

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(7)
    head.next.next.next.next = ListNode(9)
    head.next.next.next.next.next = ListNode(11)
    head.next.next.next.next.next.next = ListNode(13)
    head.next.next.next.next.next.next.next = ListNode(15)
    head.next.next.next.next.next.next.next.next = ListNode(17)
    head.next.next.next.next.next.next.next.next.next = ListNode(19)
    head.next.next.next.next.next.next.next.next.next.next = ListNode(21)

    head2 = head.next.next.next
    result = getIntersectionNode(head, head2)
    print(result.val if result is not None else None)

