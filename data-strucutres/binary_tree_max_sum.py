## Find the max sum of Binary Tree Node
## This will be simple if it is Binary Search Tree coz in that case you will always collect the left node
## Sum it up and you have the max sum of Binary Tree but in case of simple Binary Tree
## Traverse through each node find out the max value i.e.
## For each node there can be four ways that the max path goes through the node:
## 1. Node only
## 2. Max path through Left Child + Node
## 3. Max path through Right Child + Node
## 4. Max path through Left Child + Node + Max path through Right Child

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insertLeftChild(self, leftChild):
        if(self.left_child == None):
            self.left_child = BinaryTree(leftChild)
        else:
            new_node = BinaryTree(leftChild)
            new_node.left_child = self.left_child
            self.left_child = new_node
    
    def insertRightChild(self, rightChild):
        if(self.right_child == None):
            self.right_child = BinaryTree(rightChild)
        else:
            new_node = BinaryTree(rightChild)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def findMaxSum(self):
        mylist = []
        
        mylist = self.findMaxNodes(mylist, self.left_child)
        mylist.append(self.value) 
        mylist = self.findMaxNodes(mylist, self.right_child)

        return mylist
    
    def findMaxNodes(self, mylist, mynode):
        if(mynode.left_child.value > mynode.right_child.value):
            mylist.append(mynode.left_child.value)
            if(mynode.left_child.left_child and mynode.left_child.right_child):
                self.findMaxNodes(mylist, mynode.left_child)
            else:
                mylist.append(mynode.value)
        else:
            mylist.append(mynode.value)
            if(mynode.right_child.left_child and mynode.right_child.right_child):
                self.findMaxNodes(mylist, mynode.right_child)
            else:
                mylist.append(mynode.right_child.value)

        return mylist

root = BinaryTree(10) 
root.insertLeftChild(2) 
root.insertRightChild(10); 
root.left_child.insertLeftChild(20); 
root.left_child.insertRightChild(1); 
root.right_child.insertLeftChild(-25); 
root.right_child.insertRightChild(15); 
root.right_child.right_child.insertLeftChild(3); 
root.right_child.right_child.insertRightChild(4); 
print(root)
print(root.findMaxSum())

##       10
##    2       10
## 20   1  -25   15
##             3   4

## Max Sum = 20 + 2 + 10 + 10 + 15 + 4 