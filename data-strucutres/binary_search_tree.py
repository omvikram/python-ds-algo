## Just like Tree, BST will have self node, left child and right child but will have the following relation
## Left << Root << Right (this rule applies to all the node we insert as well as searching for a node)
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    ## Whenever you insert a value check if it is less than the root node then insert left
    ## Add to the left node unless you don't find any node with left node
    ## Whenever you insert a value check if it is greather than the root node then insert right
    ## Add to the right node unless you don't find any node with right node
    def insert_node(self, value):
        if value <= self.value and self.left_child: 
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)

    ## The logic remains the same, find if the node value is less then move left node
    ## if the node value is more then move right node
    ## Traverse unless you find the node equals to the search value
    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        return value == self.value

    ## We will always find the minimum value node in the left of the tree
    def find_minimum_value(self):
        if self.left_child:
            return self.left_child.find_minimum_value()
        else:
            return self.value