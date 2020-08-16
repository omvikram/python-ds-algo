class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# preorderTraversal of the tree (Root, Left, Right) => Roo-L-R
def preorderTraversal(root):
  result = []
  
  if not root:
      return result
  
  def dfs(node: TreeNode):
      if not node:
          return
      result.append(node.val)
      dfs(node.left)
      dfs(node.right)
  
  dfs(root)
  return result


# initialization of a tree
rootNode = TreeNode(1)
leftNode = TreeNode(2)
rightNode = TreeNode(3)

rootNode.left = leftNode
rootNode.right = rightNode

print('preorder: ', preorderTraversal(rootNode))
