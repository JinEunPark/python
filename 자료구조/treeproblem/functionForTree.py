from 자료구조.treeproblem.Tnode import tnode

G = tnode(None, None, 'g')
H = tnode(None, None, 'h')
E = tnode(G, H, 'e')
D = tnode(None, None, 'd')
F = tnode(None, None, 'f')
B = tnode(D, None, 'b')
C = tnode(E, F, 'c')
A = tnode(B, C, 'g')

divide = tnode(A, B, '/')
multiple_2 = tnode(divide, C, '*')
multiple = tnode(multiple_2, D, '*')
plus = tnode(multiple, E, '+')
A = tnode(None, None, 'a')
B = tnode(None, None, 'b')
C = tnode(None, None, 'c')
D = tnode(None, None, 'd')
E = tnode(None, None, 'e')


def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


def count_node(node):
    if node is None:
        return 0
    else:
        return 1 + count_node(node.left) + count_node(node.right)


def count_leaf(node):
    if node is None:
        return 0
    elif node.right == None and node.left == None:
        return 1
    else:
        return count_leaf(node.right) + count_leaf(node.left)
