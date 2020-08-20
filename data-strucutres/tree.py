## A tree is a non-linear list data structure which is represented as class in Python
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# initialization of a tree
rootNode = TreeNode(1)
leftNode = TreeNode(2)
rightNode = TreeNode(3)

rootNode.left = leftNode
rootNode.right = rightNode

## DFS (Deft First Search algo) - Going deep to the leaf and backtrack.

# inorderTraversal of the tree (Left, Root, Right) => L-Roo-R
def inorderTraversal(root):
  result = []
  
  if not root:
      return self.result
  
  def df(node: TreeNode):
      if not node:
          return
      df(node.left)
      result.append(node.val)
      df(node.right)
  
  df(root)
  return result

# preorderTraversal of the tree (Root, Left, Right) => Roo-L-R
def preorderTraversal(root):
  result = []
  
  if not root:
      return result
  
  def df(node: TreeNode):
      if not node:
          return
      result.append(node.val)
      df(node.left)
      df(node.right)
  
  df(root)
  return result

# postorderTraversal of the tree (Left, Right, Root) => L-R-Roo
def postorderTraversal(root):
  result = []
  
  if not root:
      return result
  
  def df(node: TreeNode):
      if not node:
          return
      df(node.left)
      df(node.right)
      result.append(node.val)
  
  df(root)
  return result

print('inorder: ', inorderTraversal(rootNode))
print('preorder: ', preorderTraversal(rootNode))
print('postorder: ', postorderTraversal(rootNode))