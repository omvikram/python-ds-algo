class TreeNode:
  def __init__(self, val):
    self.value = val
    self.left_child = None
    self.right_child = None

# preorderTraversal of the tree (Root, Left, Right) => Roo-L-R
def preorderTraversal(root):
  result = []
  
  if not root:
      return result
  
  def dfs(node: TreeNode):
      if not node:
          return
      result.append(node.value)
      dfs(node.left_child)
      dfs(node.right_child)
  
  dfs(root)
  return result


# initialization of a tree
rootNode = TreeNode(1)
leftNode = TreeNode(2)
rightNode = TreeNode(3)

rootNode.left_child = leftNode
rootNode.right_child = rightNode

print('preorder: ', preorderTraversal(rootNode))
