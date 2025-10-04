from common import TreeNode


def invertTree(root):

  def _swap(x , y):

    temp = y
    y = x
    x = temp
    return x , y
  
  final_ans = []

  def invert(x :TreeNode | None):
    
    if x == None : return
    final_ans.append(x.value)
    x.left , x.right = _swap(x.left , x.right)
    invert(x.left)
    invert(x.right)

  