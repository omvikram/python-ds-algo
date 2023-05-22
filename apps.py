##bootcamp file for practice
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        
    def insert_left(self, left_child_value):
        if self.left_child == None:
            self.left_child = TreeNode(left_child_value)
        else:
            new_node = TreeNode(left_child_value)
            new_node.left_child = self.left_child
            self.left_child = new_node
            
    def insert_right(self, right_child_value):
        if self.right_child == None:
            self.right_child = TreeNode(right_child_value)
        else:
            new_node = TreeNode(right_child_value)
            new_node.right_child = self.right_child
            self.right_child = new_node
                
rootNode = TreeNode(0)
leftNode = TreeNode(1)
rightNode = TreeNode(2)
rootNode.left_child = leftNode
rootNode.right_child = rightNode

rootNode.insert_left(3)
rootNode.insert_right(4)

print(rootNode.value)
print(rootNode.left_child.value)
print(rootNode.right_child.value)
print(rootNode.left_child.left_child.value)
print(rootNode.left_child.right_child.value) ##should throw an error
print(rootNode.right_child.left_child.value) ##should throw an error
print(rootNode.right_child.right_child.value)

## Main logic of preorder Roo-L-R
def preorder(root):
    resultList = []
    
    resultList.append(root.value)
    preorder(root.left_child)
    preorder(root.right_child)
    
    return resultList
    
## Main logic of inorder L-Roo-R
def inorder(root):
    resultList = []
    
    inorder(root.left_child)
    resultList.append(root.value)
    inorder(root.right_child)
    
    return resultList
    
## Main logic of postorder L-R-Roo
def inorder(root):
    resultList = []
    
    inorder(root.left_child)
    inorder(root.right_child)
    resultList.append(root.value)
    
    return resultList
    