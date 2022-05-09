# root - left - right
def preorder(n):
    if n is not None:
        print(n.data, end=" ")
        preorder(n.left)
        preorder(n.right)

# left - root - right
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=" ")
        inorder(n.right)

# left - right - root
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=" ")
