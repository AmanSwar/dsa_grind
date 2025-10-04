from common import TreeNode

def in_order(root : TreeNode | None) -> None:

    if root != None:

        in_order(root.left)
        print(root.value)
        in_order(root.right)



