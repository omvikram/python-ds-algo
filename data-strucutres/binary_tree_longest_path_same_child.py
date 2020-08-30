# Given a binary tree, find the length of the longest path where each node in the path has the same value. 
# This path may or may not pass through the root.
# The length of path between two nodes is represented by the number of edges between them.

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def arrow_length(node):
        if not node: 
            return 0

        left_length = arrow_length(node.left_child)
        right_length = arrow_length(node.right_child)

        left_arrow = right_arrow = 0

        if node.left_child and node.left_child.value == node.value:
            left_arrow = left_length + 1
        if node.right_child and node.right_child.value == node.value:
            right_arrow = right_length + 1

        return max(left_arrow, right_arrow)


root = BinaryTree(5)
root.left_child = BinaryTree(4)
root.right_child = BinaryTree(5)
root.left_child.left_child = BinaryTree(1)
root.left_child.right_child = BinaryTree(1)
root.right_child.right_child = BinaryTree(5)
#     5
#   4   5
# 1   1   5

print(arrow_length(root))