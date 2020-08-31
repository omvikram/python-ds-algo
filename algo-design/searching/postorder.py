class TreeNode:
  def __init__(self, val):
    self.value = val
    self.left_child = None
    self.right_child = None

# postorderTraversal of the tree (Left, Right, Root) => L-R-Roo
def postorderTraversal(root):
  result = []
  
  if not root:
      return result
  
  def dfs(node: TreeNode):
      if not node:
          return
      dfs(node.left_child)
      dfs(node.right_child)
      result.append(node.value)
  
  dfs(root)
  return result


# initialization of a tree
rootNode = TreeNode(1)
leftNode = TreeNode(2)
rightNode = TreeNode(3)

rootNode.left_child = leftNode
rootNode.right_child = rightNode

print('postorder: ', postorderTraversal(rootNode))
