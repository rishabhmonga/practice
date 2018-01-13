import math


class Node:
    # Utility function to create a new tree node
    def __init__(self, key, color):
        self.key = key
        self.child = []
        self.color = color
        self.rb_score = 0


global max_black_parent


def printNodeLevelWise(root):
    if root is None:
        return
    queue = [root]
    while len(queue) > 0:

        n = len(queue)
        while (n > 0):
            p = queue[0]
            queue.pop(0)
            print(p.key, '->', p.rb_score, end=' ')
            for index, value in enumerate(p.child):
                queue.append(value)
            n -= 1
        print()


def set_rb_score(node):
    if node is None:
        return 0

    child_score = 0
    global max_black_parent
    for child_node in node.child:
        child_node.rb_score += set_rb_score(child_node)
        child_score += child_node.rb_score

    if node.color == 'black':
        node.rb_score += 1 + child_score
    elif node.color == 'red':
        return -math.inf
    if node.rb_score > max_black_parent.rb_score:
            max_black_parent = node
    return node.rb_score


if __name__ == '__main__':
    root = Node(10, 'red')
    root.child.append(Node(5, 'black'))
    root.child.append(Node(15, 'red'))
    root.child.append(Node(20, 'black'))
    root.child.append(Node(11, 'black'))
    root.child[2].child.append(Node(18, 'red'))
    root.child[2].child.append(Node(16, 'black'))
    root.child[3].child.append(Node(24, 'red'))
    root.child[3].child.append(Node(3, 'black'))
    root.child[3].child.append(Node(65, 'black'))
    # root.child[3].child[2].child.append(Node(4, 'black'))
    # root.child[2].child[0].child.append(Node(47, 'black'))
    # root.child[2].child[1].child.append(Node(7, 'black'))

    max_black_parent = root
    set_rb_score(root)

    printNodeLevelWise(root)

    print("This : " + str(max_black_parent.key) + " -> " + str(max_black_parent.rb_score))
