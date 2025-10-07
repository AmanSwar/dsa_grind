from common import TreeNode

def lowestCommonAncestor(root , p , q):

    if root == None or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left , p, q)
    right = lowestCommonAncestor(root.right , p, q)

    if left and right:
        return root
    
    return left or right




# def lowestCommonAncestor(root : TreeNode , p , q) -> TreeNode:

#   ancestors = {}
#   ans_node = None
#   def _dfs(node : TreeNode):
#     nonlocal p , q , ancestors , ans_node

#     if node == None : return

#     if node.value == p: return 1
#     if node.value == q : return 1

#     l = _dfs(node.left)

#     if l == 1:
#       if ancestors.get(node.value , 0) > 1:
#         ans_node = node
#         return
#       ancestors[node.value] = ancestors.get(node.value , 0) + 1
#       return 1

#     r = _dfs(node.right)
#     if r == 1:
#       if ancestors.get(node.value , 0) > 1:
#         ans_node = node
#         return
#       ancestors[node.value] = ancestors.get(node.value , 0) + 1
#       return 1

#     return 0

#   return ans_node
