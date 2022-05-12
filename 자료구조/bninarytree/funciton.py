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
        print(node.data, end=' ')#현재 가운데 노드의 데이터를먼저 출력한다.
        preorder(node.left)#노드의 왼쪽 자식으로 순회함
        preorder(node.right)#노드의 오른쪽 자시긍로 순회함


def postorder(node):  # LRV
    if node is not None:
        postorder(node.left)#노드의 왼쪽자식을 우선적으로 순회함
        postorder(node.right)#노드의 오른쪽 자식을 순회함.
        print(node.data, end=" ")#현재 가운데 노드의 데이터를 출력한다.


def inorder(node):  # LVR
    if node is not None:
        inorder(node.left)#왼쪽 노드를 우선을 순회함.
        print(node.data, end=" ")#현재 노드를 순횐함
        inorder(node.right)#오른쩍 노드를 순회함.


def leveorder(node):#원형 큐를 이용해서

    c = circleQueue()#원형 큐 객체를 생성한다.
    c.enquene(node)#root를 먼저 큐에 삽입한다.

    while not c.isEmpty():#원형큐가 빌때까지 반복한다.

        n = c.dequene()#제일 처음에 삽입햇던 루트 노드를반환한다.

        if n is not None:
            print(n.data, end=" ")#가장먼저 들어간 노드의 출력
            c.enquene(n.left)#노드의 왼쪽 자식 삽입
            c.enquene(n.right)#노드의 오른쩍 자식 십입

def count_node(node):#노드의 갯수를 반환하는 함수
    if node is None:
        return 0
    else:
        return 1 + count_node(node.left) + count_node(node.right)#노드를 하나 지날 때 마다 +1 이된다 근데 이때 반환하는 값이
    #다른 왼쪽 자식을 을 먼저 순회하고 그 다음에 오른쪽 자신을 순횐한다.

def count_terminalNode(node):#말단 노드의 갯수를 반환하는 함수
    if node is None:#현재 대상노드가 none이면 0을 반환한다. 빈트리를 새지 않는다
        return 0
    elif node.left is None and node.right is None:#현재 자기 자신 주위의 자식노드들이 하나도 없으면 말단 노드 이므로 하나를 추가한다.
        return 1
    else:
        return count_terminalNode(node.left) + count_terminalNode(node.right)#둘다 아니고 말단노드가 아니라면 양쪽노드로 순횐한다.


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