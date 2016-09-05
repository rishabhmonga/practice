# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        nextNode = None
        while curr is not None :
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        head = prev
        return head

    @staticmethod
    def printList(start):
        while start is not None:
            print(start.val)
            start = start.next
        print("\n")

soln = Solution()
inputNode = ListNode(1)
inputNode.next = ListNode(2)
inputNode.next.next = ListNode(3)
inputNode.next.next.next = ListNode(4)
soln.printList(inputNode)
inputNode = soln.reverseList(inputNode)
soln.printList(inputNode)
