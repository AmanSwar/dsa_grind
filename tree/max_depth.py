from common import TreeNode

def maxDepth(root : TreeNode):

  max_dia = 0

  def _dfs(node):
    nonlocal max_dia
    if node == None : return 0

    left_height = _dfs(node.left)
    right_height = _dfs(node.right)

    max_dia = max(max_dia , left_height + right_height)
    
    return 1 + max(left_height , right_height)
  
  _dfs(root)
  return max_dia

