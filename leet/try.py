class LinkedList:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(node):
    while node is not None:
        print(node.val)
        node = node.next


def delete_element(val, root):
    new_root = root
    if root.val == val:
        new_root = root.next
        root.next = None
        return new_root
    prev = root
    while root is not None:
        if root.val != val:
            root = root.next
        else:
            prev.next = root.next
            break
    return new_root

if __name__ == '__main__':
    print(45 // 2)
    ll = LinkedList(1)
    ll.next = LinkedList(2)
    ll.next.next = LinkedList(3)
    ll.next.next.next = LinkedList(4)
    ll.next.next.next.next = LinkedList(5)
    print_list(ll)
    print()
    root = delete_element(3, ll)
    print_list(root)
