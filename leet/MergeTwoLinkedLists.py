from leet.ListNode import ListNode


class Solution(object):
    def mergeTwoLists(self, l1, l2):
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


root1 = ListNode(1)
root1.next = ListNode(3)
root1.next.next = ListNode(4)
ListNode.printList(root1)

root2 = ListNode(0)
ListNode.printList(root2)
soln = Solution()
result = soln.mergeTwoLists(root1, root2)
ListNode.printList(result)
