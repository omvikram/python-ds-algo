class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# postorderTraversal of the tree (Left, Right, Root) => L-R-Roo
def postorderTraversal(root):
  result = []
  
  if not root:
      return result
  
  def dfs(node: TreeNode):
      if not node:
          return
      dfs(node.left)
      dfs(node.right)
      result.append(node.val)
  
  dfs(root)
  return result


# initialization of a tree
rootNode = TreeNode(1)
leftNode = TreeNode(2)
rightNode = TreeNode(3)

rootNode.left = leftNode
rootNode.right = rightNode

print('postorder: ', postorderTraversal(rootNode))
