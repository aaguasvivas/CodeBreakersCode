def inorder(root, arr):
    if root is None:
        return
    inorder(root.left)
    arr.append(root.val)
    inorder(root.right)


def reverse_inorder(root):
    if root is None:
        return
    reverse_inorder(root.right)
    arr.append(root.val)
    reverse_inorder(root.left)


def preorder(root):
    if root is None:
        return
    arr.append(root.val)
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    arr.append(root.val)
