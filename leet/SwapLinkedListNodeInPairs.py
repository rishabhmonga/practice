from leet.ListNode import ListNode


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        firstNode = head
        secondNode = head.next
        firstNode.next = secondNode.next
        secondNode.next = firstNode
        head = secondNode
        secondNode = firstNode.next
        while firstNode.next is not None and secondNode.next is not None:
            temp = secondNode.next
            firstNode.next = temp
            secondNode.next = temp.next
            temp.next = secondNode
            firstNode = secondNode
            secondNode = firstNode.next
        return head


soln = Solution()
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
ListNode.printList(root)
root = soln.swapPairs(root)
ListNode.printList(root)
