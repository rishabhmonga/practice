# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        curr = head
        nextNode = head.next
        while curr is not None and nextNode is not None:
            if curr.val == nextNode.val:
                curr.next = nextNode.next
                nextNode = curr.next
                continue
            curr = curr.next
        return head

    @staticmethod
    def printList(first):
        while first is not None:
            print(first.val)
            first = first.next
        print("\n")

soln = Solution()
start = ListNode(1)
# start.next = ListNode(2)
# start.next.next = ListNode(3)
# start.next.next.next = ListNode(3)
# start.next.next.next.next = ListNode(4)
# start.next.next.next.next.next = ListNode(5)
# start.next.next.next.next.next.next = ListNode(5)
start.next = ListNode(1)
start.next.next = ListNode(1)
Solution.printList(start)
start = soln.deleteDuplicates(start)
Solution.printList(start)
