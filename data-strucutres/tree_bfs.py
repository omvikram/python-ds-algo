## A tree is a non-linear list data structure which is represented as class in Python
## BFS (Breadth First Search algo) - Traverse through each level nodes
## Recursive Python program for level order traversal of Binary Tree 

class TreeNode():

    def __init__(self, val):
        self.value = val
        self.left_child = None
        self.right_child = None

## Find the height of the tree recursively and then 
## print each level nodes based on the height from root to leaf nodes
def printLevelOrderNodes(root):
    height = calculateHeight(root)
    
    print("Level order traversal of Tree of height {}".format(height))
    
    for h in range(1, height+1):
        printSpecificLevelNodes(root, h)

def calculateHeight(node):
    if(node == None):
        return 0

    left_height = calculateHeight(node.left_child)
    right_height = calculateHeight(node.right_child)

    if(left_height > right_height):
        return left_height + 1
    else:
        return right_height + 1

def printSpecificLevelNodes(node, level):
    if(node == None):
        return
    
    if(level == 1):
        print(node.value)
    elif(level > 1):
        printSpecificLevelNodes(node.left_child, level-1)
        printSpecificLevelNodes(node.right_child, level-1)

        
root = TreeNode(1) 
root.left_child = TreeNode(2) 
root.right_child = TreeNode(3) 
root.left_child.left_child = TreeNode(4) 
root.left_child.right_child = TreeNode(5) 
   
printLevelOrderNodes(root)