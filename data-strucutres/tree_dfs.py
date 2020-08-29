## A tree is a non-linear list data structure which is represented as class in Python
## DFS (Deft First Search algo) - Going deep to the leaf and backtrack.

class TreeNode:
  def __init__(self, val):
    self.value = val
    self.left_child = None
    self.right_child = None

# initialization of a tree
rootNode = TreeNode(1)
leftNode = TreeNode(2)
rightNode = TreeNode(3)

rootNode.left_child = leftNode
rootNode.right_child = rightNode

# preorderTraversal of the tree (Root, Left, Right) => Roo-L-R
def preorderTraversal(root):
  result = []
  
  if not root:
      return result
  
  def dfs(node):
      if not node:
          return
      result.append(node.value)
      dfs(node.left_child)
      dfs(node.right_child)
  
  dfs(root)
  return result

# inorderTraversal of the tree (Left, Root, Right) => L-Roo-R
def inorderTraversal(root):
  result = []
  
  if not root:
      return self.result
  
  def dfs(node):
      if not node:
          return
      dfs(node.left_child)
      result.append(node.value)
      dfs(node.right_child)
  
  dfs(root)
  return result

# postorderTraversal of the tree (Left, Right, Root) => L-R-Roo
def postorderTraversal(root):
  result = []
  
  if not root:
      return result
  
  def dfs(node):
      if not node:
          return
      dfs(node.left_child)
      dfs(node.right_child)
      result.append(node.value)
  
  dfs(root)
  return result

print('inorder: ', inorderTraversal(rootNode))
print('preorder: ', preorderTraversal(rootNode))
print('postorder: ', postorderTraversal(rootNode))