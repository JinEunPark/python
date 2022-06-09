from 자료구조.btree.TNODE import tnode

F = tnode('F', None, None)
E = tnode('E', None, None)
D = tnode('D', None, None)
B = tnode('B', D, E)
C = tnode('C', F, None)
A = tnode('A', B, C)


# 순회 3가지 전위순회 , 중위순회, 후휘순회, 레벨순위
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


def leveltrival(node):
    list = []
    list.append(node)
    while len(list) != 0:
        node = list.pop(-1)
        if node is not None:
            print(node.data, end=" ")
            list.insert(0, node.left)
            list.insert(0, node.right)


# 트리의 높이를 반환하는 함수, 트리의 터미널 노드의 갯수를 반환하는 함수, 트리의
def count_node(node):
    if node is None:
        return 0
    else:
        return 1 + count_node(node.left) + count_node(
            node.right)  # if node is not None return sum of left and right node count


def count_leaf(node):
    if node is None:
        return 0
    elif node.left is None and node.right is None:
        return 1
    else:
        return 0 + count_leaf(node.left) + count_leaf(node.right)  #


def getHeight(node):
    if node is None:
        return 0
    Lhight = getHeight(node.left)
    Rhight = getHeight(node.right)

    if Lhight > Rhight:
        return 1 + Lhight
    else:
        return 1 + Rhight


print("result of preoder:")
preorder(A)
print()
print("result of inorder:")
inorder(A)
print()
print("result of postorder:")
postorder(A)
print("height of this tree: %d" % (getHeight(A)))
print("count of node", count_node(A))
print("count of terminal node:", count_leaf(A))
