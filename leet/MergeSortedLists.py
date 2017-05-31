# Definition for singly-linked list.
from queue import PriorityQueue


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


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    if l1.val <= l2.val:
        rootVal = l1.val
        l1 = l1.next
    else:
        rootVal = l2.val
        l2 = l2.next
    root = ListNode(rootVal)
    nextNode = root
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            nextNode.next = ListNode(l1.val)
            l1 = l1.next
        elif l1.val > l2.val:
            nextNode.next = ListNode(l2.val)
            l2 = l2.next
        nextNode = nextNode.next
    while l1 is not None:
        nextNode.next = ListNode(l1.val)
        l1 = l1.next
        nextNode = nextNode.next
    while l1 is not None:
        nextNode.next = ListNode(l2.val)
        l2 = l2.next
        nextNode = nextNode.next
    return root


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    i = 0
    while i < len(lists):
        if lists[i] is None:
            del lists[i]
            i -= 1
        i += 1
    list_length = len(lists)
    while list_length > 1 and list_length != 0:
        merged_list = []
        if list_length % 2 != 0:
            lists.append(None)
            list_length += 1
        idx = 0
        while idx < list_length - 1:
            merged_list.append(mergeTwoLists(lists[idx], lists[idx + 1]))
            idx += 2
        list_length /= 2
        lists = merged_list
    return lists[0] if lists else None


def merge2(lists):
    dummy = ListNode(None)
    curr = dummy
    q = PriorityQueue()
    for node in lists:
        if node:
            q.put((node.val, node))
    while q.qsize() > 0:
        curr.next = q.get()[1]
        curr = curr.next
        if curr.next:
            q.put((curr.next.val, curr.next))
    return dummy.next


if __name__ == '__main__':
    root1 = ListNode(1)
    root1.next = ListNode(3)
    root1.next.next = ListNode(4)
    # ListNode.printList(root1)

    root2 = ListNode(2)
    # ListNode.printList(root2)

    root3 = ListNode(0)
    # ListNode.printList(root3)

    results = mergeKLists([root1, root2, root3])
    # results = mergeKLists([root1, root3])
    # results = merge2([root1, root2, root3])
    # results = mergeKLists([None, None])

    ListNode.printList(results)
