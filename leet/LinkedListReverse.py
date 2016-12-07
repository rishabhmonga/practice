"""
prev = None
next = None
while curr not None:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
return prev


# recursive

first = None
rest = None
if head is None:
    return
first = head
rest = first.next
if rest is None:
    return
recursive_reverse(rest)
first.next.next = first
first.next = None
head = rest

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse(head):
    curr = head
    prev = None
    nextNode = None
    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev


def recursive_reverse(head):
    if head is None:
        return None
    if head.next is None:
        return head
    rest = recursive_reverse(head.next)
    head.next.next = head
    head.next = None
    return rest


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    print_list(head)
    root = reverse(head)
    print_list(root)
    root = recursive_reverse(root)
    print_list(root)
