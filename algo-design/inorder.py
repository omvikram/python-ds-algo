class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# inorderTraversal of the tree (Left, Root, Right) => L-Roo-R
def inorderTraversal(root):
  result = []
  
  if not root:
      return result
  
  def dfs(node: TreeNode):
      if not node:
          return
      dfs(node.left)
      result.append(node.val)
      dfs(node.right)
  
  dfs(root)
  return result


# initialization of a tree
rootNode = TreeNode(1)
leftNode = TreeNode(2)
rightNode = TreeNode(3)

rootNode.left = leftNode
rootNode.right = rightNode

print('inorder: ', inorderTraversal(rootNode))
