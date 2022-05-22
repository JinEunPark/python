from 자료구조.BSTrecursice.bstNode import bnode

a = bnode(8, 'A')
b = bnode(3, 'B')
c = bnode(1, 'C')
d = bnode(5, 'B')
e = bnode(4, 'E')
f = bnode(9, 'F')
g = bnode(11, 'G')
h = bnode(12, 'H')

list = [a, b, c, d, e, f, g, h]


def insert_bst(compareNode, newNode):
    if compareNode == None:
        return True
    if compareNode.key < newNode.key:
        if compareNode.right == None:
            compareNode.right = newNode
            return True
        else:
            return insert_bst(compareNode.right, newNode)
    elif compareNode.key > newNode.key:
        if compareNode.left == None:
            compareNode.left = newNode
            return True
        else:
            return insert_bst(compareNode.left, newNode)
    else:
        return False


def search_value_repeat(node, key):
    while node != None:
        if node.key < key:
            node = node.right
        elif node.key > key:
            node = node.left
        elif node.key == key:
            return node


def search_value(compareNode, key):
    if compareNode.key == key:
        return compareNode
    elif compareNode.key < key:
        return search_value(compareNode.right, key)
    else:
        return search_value(compareNode.left, key)


def show_bst(node):
    if node is not None:
        show_bst(node.left)
        print(node.key, end=" ")
        show_bst(node.right)


def delete_bst_case1(parent, node, root):  # 삭제가할 노드가 단말 노드라는 가정하에 진행

    if parent is None:  # 부모 노드가 없다는 것은 삭제할 단말노드가 root란 소리고 그러면 트리가 소멸한다.
        root = None
    else:
        if parent.left == node:  # 삭제할 노드가 부모 노드의 왼쪽 노드이먄 부모 노드의 왼쪽 링크를 삭제한다.
            # 근데 위에 비교연산을 설정한 적이 없는데 어케 되는건지 모르겠다.
            parent.left = None
        else:
            parent.right = None
    return root  # root의 변경이 일어날지도 몰라서 반환


def delete_bst_case2(parent, node, root):  # 삭제할 대상의 node가 자식이 있는데 왼쪽이나 오른쪽이나 하나만 가지는 경우

    if node.left is not None:  # 삭제할 노드가 왼쪽 자식만을 가지는 경우
        child = node.left  # 자기 자식의 왼쪽 노드를 child 변수에 담는다.
    else:
        child = node.right  # 삭제하려는 노드가 오른쪽 노드만을 가지는 경우에는 자신의 오른쪽 자식을 child 변수에 할당한다.

    if node == root:  # 삭제하려는 node가 root와 같다면
        root = child  # cild 에 root를 할당한다.
    else:

        if node is parent.right:  # 삭제하려는 노드가 부모 노드의 오른쪽 자식이라면 부모의 right fild에 child를 담는다
            # 메모리를 가리키는 표인터가 존재하지 않게되어서 저절로 사라진다.
            parent.right = child
        else:
            parent.left = child
            # 삭제하려는 node가 부모 노드의 왼쪽 자식이라면 부모의 왼쪽 필드에 삭제하려는 node의 child노드를 할당한다.
    return root


def delete_bst_case3(parent, node, root):  # parameter1: parentnode parameter2: need to be delete parameter3: root
    succp = node  # 삭제할 노드를 후계자 노드의 부모 노드로 설정
    succ = node.right  # 삭제할 노드의 오르쪽 자식을 후계자 노드로 설정

    while (succ.left != None):  # 후계자 노드의 왼쪽 자식이 None일 때 까지
        succp = succ  # 부모노드를 자식 노드로 바꿈
        succ = succ.left  # 후계자 노드의 왼쪽 노드를 후계가 노드로 설정 점점 내려간다.

    if (succp.left == succ):
        succp.left = succ.right
    else:  # 이미 succ.left  = None 양쪽에 둘다 자식이 없던것임
        succp.right = succ.right  # None 값이 succp의 오른쪽 자식에 대입됨

    node.key = succ.key  # 삭제할 node에 succesor 의 자식을 복산한다.
    node.value = succ.value  # 삭제할 node succesor의 자식을 복사한다.
    node = succ  # 함수가 종료 되면서 succ는 연결되어 있는 부모의 링크를 잃었기 땜에 삭제된다. 근데 이게 필요한건지 모르겠음.
    return root


def delelte_bst(root, key):
    if root == None:
        return None
    parent = None
    node = root
    while node != None and node.key != key:
        parent = node
        if key < node.key:
            node = node.left
        else:
            node = node.right
    if node is None: return None
    if node.left is None and node.right is None:
        root = delete_bst_case1(parent, node, root)
    elif node.left is None or node.right is None:
        root = delete_bst_case2(parent, node, root)
    else:
        root = delete_bst_case3(parent, node, root)


insert_bst(None, a)
for i in range(1, len(list)):
    insert_bst(a, list[i])
show_bst(a)
delelte_bst(a,1)
delelte_bst(a,11)
delelte_bst(a,12)
print()
show_bst(a)

