# Given the root node of a binary search tree, 
# return the sum of values of all nodes with value between L and R (inclusive).

# The binary search tree is guaranteed to have unique values.
# Example :
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self, value):
        if value <= self.value and self.left_child: 
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)

#BST works on the primary principle i.e. L << Roo << R
def dfs(node, L, R, path):
    if node:
        if(L <= node.value <= R):
            path.append(node.value)
        if(L < node.value):
            dfs(node.left_child, L, R, path)
        if(node.value < R):
            dfs(node.right_child, L, R, path)
    return path

#Example 1
root = BinarySearchTree(10)
root.insert_node(5)
root.insert_node(15)
root.insert_node(3)
root.insert_node(7)
root.insert_node(None)
root.insert_node(18)
path = []
print(dfs(root, 7, 15, path))
