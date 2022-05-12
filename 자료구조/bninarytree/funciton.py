from 자료구조.bninarytree.Tnode import treeNode
from 자료구조.bninarytree.circlequeue import circleQueue

H = treeNode(None, None, 'h')
I = treeNode(None, None, 'i')
J = treeNode(None, None, 'j')
K = treeNode(None, None, 'k')
D = treeNode(H, I, 'd')
E = treeNode(None, None, 'e')
B = treeNode(D, E, 'b')
G = treeNode(J, K, 'g')
F = treeNode(None, None, 'f')
C = treeNode(F, G, 'c')
A = treeNode(B, C, 'a')


def preorder(node):  # VLR
    if node is not None:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)


def postorder(node):  # LRV
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


def inorder(node):  # LVR
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


def leveorder(node):

    c = circleQueue()
    c.enquene(node)

    while not c.isEmpty():

        n = c.dequene()

        if n is not None:
            print(n.data, end=" ")
            c.enquene(n.left)
            c.enquene(n.right)

def count_node(node):
    if node is None:
        return 0
    else:
        return 1 + count_node(node.left) + count_node(node.right)

def count_terminalNode(node):
    if node is None:
        return 0
    elif node.left is None and node.right is None:
        return 1
    else:
        return count_terminalNode(node.left) + count_terminalNode(node.right)


print("preorder", end=" ")
preorder(A)
print()
print("inorder", end=" ")
inorder(A)
print()
print("posterorder", end=" ")
postorder(A)
print("levelorder ", end=" ")
leveorder(A)
print()
print("number of node in tree", count_node(A))
print("number of terminal node", count_terminalNode(A))