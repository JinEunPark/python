from 자료구조.bsttest.bstNODE import bnode

A = bnode(35, 'A')
B = bnode(18, 'B')
C = bnode(68, 'C')
D = bnode(7, 'D')
E = bnode(26, 'E')
F = bnode(99, 'F')
G = bnode(3, 'G')
H = bnode(12, 'H')
I = bnode(22, 'I')
J = bnode(30, 'J')

list = [B, C, D, E, F, G, H, I, J]


# bst에서 값을 찾는 함수 순환을 이용
def search_bst(node, key):
    if node == None:  # 탐색트리 안에 같은 값이 존재하지 않는경우
        return None
    if key == node.key:  # 같은 키를 찾은경우
        return node
    elif key > node.key:
        search_bst(node.right, key)  # 키값이 비교하는 노드보다 큰경우 오른쪽 자식을 기준으로 함수 다시 호출
    else:
        search_bst(node.left, key)  # 키값이 비교하는 노드보다 작은경우 왼쪽을 자식을 기준으로 함수 다시 호출


# bst에서 값을 찾는함수 반복문을 사용함
def search_bst_iter(node, key):
    while node is not None:  # while문이 끝나면 같은 키를 찾지 못한거임
        if node.key == key:  # 찾음
            return node
        if node.key < key:  # 키가 더 큰경우
            node = node.right  # 오른쪽 자식을 기준으로 변경
        else:
            node = node.left  # 왼쪽 자식을 기준으로 변경
    return None


# 최대값을 찾는 함수
def find_max(node):
    while node != None and node.right != None:  # node의 오른쪽 자식이 None일때까지 이동
        node = node.right  # 오른쪽 자식이 None일때 반복문이 종료됨
    return node


# 최소값을 찾는 함수
def find_left(node):
    while node != None and node.left != None:  # 왼쪽 자식이 None일때 반복문이 종료된다.
        node = node.left
    return node


def insert(root, node):
    if root.key < node.key:  # 노드의 키값이 더 작은경우
        if root.right is None:  # 노드의 오른쪽 자식이 비어있는경우 그자리에 삽입
            root.right = node
            return True  # 삽입에 성공하면 True를 반환한다.
        else:
            insert(root.right, node)  # 비어있지 않으면 오르쪽 자식을 기준으로 함수 다시 호출
    elif root.key > node.key:  # 찾으려는 키값이 더 작은경우
        if root.left is None:  # 왼쪽 자식이 비어 있는 경우에서는 그자리에 삽입한다.
            root.left = node
            return True
        else:
            insert(root.left, node)  # 왼쪽 자리가 비어있지 않은 경우 왼쪽 자식을 기준으로 함수 제호출
    else:
        return False  # 같은 키값을 가진 노드가 있는 경에는False삽입이 불가능하고 중복을 허용하지 않는다.


def delete_bst_case1(root, node, parent):  # 자식이 없는 단말노드의 삭제

    if parent is None:  # 부모 노드가 앖다는 건 parent가 제일 상단의 root라는 소리고 빈 트리가 된다.
        root = None
    else:
        if parent.left == node.key:  # 부모의 어느쪽 자식인지 파악하고 바로 삭제
            parent.left = None  # 링크를 공백으로 바꾼다.
        else:
            parent.right = None
    return root


def delete_bst_case2(root, node, parent):
    if parent.right == node:
        if node.right is None:
            parent.right = node.left
        else:
            parent.right = node.right
    else:
        if node.right is None:
            parent.left = node.left
        else:
            parent.left = node.right
    return root


def delete_bst_case3(root, node, parent):
    succ = node.right
    succp = node

    while succ.left != None:
        succp = succ
        succ = succ.left

    if succp.left == succ:
        succp.left = succ.right
    else:
        succp.right = succ.right
    node.key = succ.key
    node.value = succ.value
    node = succ

    return root


def delete(root, key):
    # 트리가 공백인경우
    if root is None:
        return None

    parent = None
    node = root
    while node.key != key and node is not None:
        parent = node
        if node.key < key:
            node = node.right
        else:
            node = node.left
    if node == None:
        return None
    if node.right is None and node.left is None:
        delete_bst_case1(root, node, parent)
    elif node.right is None or node.left is None:
        delete_bst_case2(root, node, parent)
    else:
        delete_bst_case3(root, node, parent)


def display(root):
    if root is not None:
        display(root.left)
        print(root.key, end=" ")
        display(root.right)


def count_node(node):
    if node is None:
        return 0
    else:
        return 1 + count_node(node.left) + count_node(node.left)


def search_node(node, key):
    if node == None:
        return None
    if node.key == key:
        return node
    elif node.key > key:
        search_node(node.left, key)
    elif node.key < key:
        search_node(node.right, key)


for i in range(9):
    insert(A, list[i])
display(A)
print()
for i in range(3):
    delete(A, list[i].key)
display(A)


class BstMap():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def clear(self):
        self.root = None

    def size(self):
        return count_node(self.root)

    def search(self, key):
        return search_node(self.root, key)

    def search_value(self, key):
        node = search_node(key)
        return node.value

    def findMax(self):
        return find_max(self.root)

    def findMin(self):
        return find_left(self.root)

    def insert(self, key, value=None):
        newNode = bnode(key, value)
        if self.isEmpty():
            self.root = newNode
        else:
            insert(self.root, newNode)

    def delete(self, key):
        if self.isEmpty():
            return None
        else:
            delete(self.root, key)

    def display(self):
        display(self.root)


bstmap = BstMap()
data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
print()
for i in data:
    bstmap.insert(i)
bstmap.display()
for i in range(1,6):
    bstmap.delete(data[i])
print()
bstmap.display()