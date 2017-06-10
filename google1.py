# Please use this Google doc to code during your interview. To free your hands for coding, we recommend that you use a headset or a phone with speaker option.
#
# Write a function that accepts a string and returns the reverse of it.
#
# Example: Given "abcde", returns "edcba".

def reverse_string(str1):
	str2 = ‘’
	for i in reversed(str1):
		str2 += i
	return str2
# 
# Given a full binary tree containing ones and zeros, verify that it follows the following rule:
#
# For each node, if both child nodes have the same value, that node's value is 0. If both child nodes have different values, that node's value is 1.
#
#
# Example that follows the rule:
#
#               1
#             /   \
#           /       \
#         /           \
#       0               1
#     /   \           /   \
#   1       1       1       0
#  / \     / \     / \     / \
# 0   1   0   1   1   0   1   1
#
#
# Example that breaks the rule:
#
#               0
#             /   \
#           /       \
#         /           \
#       1               1  <--WRONG
#     /   \           /   \
#   0       1       0       0
#  / \     / \     / \     / \
# 1   1   0   1   0   0   1   1
#

class tree():
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

def rule_check(root):
	if root is None:
		return true
	from collections import deque
	nodes = deque()
	nodes.append(root)
	current_node = None
	while len(nodes) != 0:
		current_node = nodes.popleft()
		if current_node.left is not None and current_node.right is not None:
			if current_node.left.val == current_node.right.val and current_node.val == 1:
				return false
			elif current_node.left.val != current_node.right.val and current_node.val == 0:
				return false
		else:
				nodes.append(current_node.left)
				nodes.append(current_node.right)

	return true


# nodes : root[0]

# Part 2:
# Write a function to flip the value of a leaf.
class tree():
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

def flip_value(node):
	node.val = 1 if node.val == 0 else 0
	return node

def rule_check(root, leaf):
	leaf = flip_value(leaf)
	if root is None:
		return true
	from collections import deque
	nodes = deque()
	nodes.append(root)
	current_node = None
	while len(nodes) != 0:
		current_node = nodes.popleft()
		if current_node.left is not None and current_node.right is not None:
			if current_node.left.val == current_node.right.val and current_node.val == 1:
				current_node = flip_value(current_node)
			elif current_node.left.val != current_node.right.val and current_node.val == 0:
				current_node = flip_value(current_node)

			nodes.append(current_node.left)
			nodes.append(current_node.right)
	return root



# Example that follows the rule:
#
#               1
#             /   \
#           /       \
#         /           \
#       0               1
#     /   \           /   \
#   1       0       1       0
#  / \     / \     / \     / \
# 0   1   1   1   1   0   1   1
#         ^^ - flip

main():
	rule_check(root, leaf)
