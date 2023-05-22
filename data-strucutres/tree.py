## A tree is a non-linear list data structure which is represented as class in Python
## A tree will have its value and child nodes which is of tree class
## A rootNode with LeftNode and RightNode

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left_child = None
        self.right_child = None
   
    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.right_child = self.right_child
            self.right_child = new_node


# initialization of a tree
rootNode = TreeNode(1)
leftNode = TreeNode(2)
rightNode = TreeNode(3)

rootNode.left_child = leftNode
rootNode.right_child = rightNode

print("Tree before insertion")
print(rootNode.value)
print(rootNode.left_child.value)
print(rootNode.right_child.value)

rootNode.insert_left(4)
rootNode.insert_right(5)

print("Tree after insertion")
print(rootNode.value)
print(rootNode.left_child.value)
print(rootNode.right_child.value)
print(rootNode.left_child.left_child.value)
print(rootNode.right_child.right_child.value)
