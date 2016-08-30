# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def printList(node):
        while node is not None:
            print(node.val, end=" ")
            node = node.next
        print("\n")


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)

ListNode.printList(root)
result = Solution()
result.deleteNode(root.next.next)

ListNode.printList(root)
