from 자료구조.newBst.newB import Bnode


def search_bst(node, key):
    if node is None:  # 끝까지 못찾아서 node == 0이면 None을 반환
        return None
    elif node.key == key:  # 현재 노드과 키값이 같으면 현재 노드를 반환한다.
        return node
    elif node.key < key:  # 현재 키값이 크다면 탐색방향을 오른쪽으로 튼다.
        return search_bst(node.right, key)
    else:
        return search_bst(node.left, key)  # 작으면 왼쪽으로 튼다


def search_bst_iter(node, key):
    while node is not None:
        if node.key == key:
            return node
        elif node.key < key:
            node = node.right
        else:
            node = node.left


def search_value(node, value):  # 키값을 이용해서 순회하는 것이 아니기 때문에 모든 노들를 방문해야하는데 이 때문에 시간 복잡도가 증가한다.
    # 중우순회 전위순회 후위순회 어떤 방법으로 순회를 해도 관계가 없다
    if node is None:
        return None
    elif value == node.value:
        return node
    res = search_bst(node.left, value)  # 일단 반환하는 값을받아
    if res is not None:  # 만약에 반환하는 값이 none이면
        return res
    else:
        return search_bst(node.right, value)  # 오른쪽 값을 반환해
    # 근데 이때 오르쪽도 반환하는 값이 none이면 반환하느 ㄴ값이 초종적으로는 0이 되는거야 아니면 둘중에 하나에서 none가 아닌값을 반환하면
    # 그 값이 반환하는 값이 되는거야 굳야 양쪽을 둘다 확인하라 필요가 없는거지
    # 알겠이 진은아.


def insert_bst(root, node):
    if root.key > node.key:  # 삽입하는 노드의 키값 보다 root의 키값이 크다면
        if root.left == None:  # root 노드의 왼쪽 자식이 공백이라면 삽입
            root.left = node
            return True
        else:
            insert_bst(root.left, node)  # 공백이 아니라면 root.left로 이동해서 순환호출
    if root.key < node.key:  # 찾는 노드의 키값이 루트보다 더 크다면
        if root.right == None:  # 부모 노드의 오른쪽이 비었다면 새로운 노드 삽입
            root.right = node
            return True
        else:
            insert_bst(root.right, node)  # 아니면 다시 오른쪽 노드로 바꿔서 호출
    if root.key == node.key:  # 키값반환
        return False


def find_max(node):
    while node != None and node.right != None:  # node가 마지막 노드가 아닐때 까지오른쪽 노드로 이동
        node = node.right
    return node


def find_min(node):
    while node != None and node.left != None:  # 왼쪽으로 가야 작기 때문에 왼쪽으로 이동
        node = node.left
    return node


def delete_bst_case1(parent, root, node):  # 단말 노드를 삭제하는 경우
    if parent == None:  # 부모 노드가 None 이라는 거는 node가 root라는 거고 root를 삭제하면 빈 트리를 반환하게 된다.
        root = None
    else:

        if parent.right == node:  # 만일 부모의 오른쪽 자식이라면
            parent.right = None
        else:
            parent.left = None

    return root


def delete_bst_case2(parent, root, node):  # 자식이 왼쪽에 있는 놈을 삭제하는 경우
    # 삭제하려는 자식 노드가 왼쪽 자식이거나 오른쪽 자식인경우
    if node.left is None:  # 노드가 왼쪽 자식만 가진경우
        child = node.left
    else:  # 노드가 오른쪽 자식만을 가진경우
        child = node.right
    if root == node:  # 삭제하려는 노드가 root이면 root에 child를 넣는다.
        root = child
    if node == parent.left:  # 노드가 부모노드의 왼쪽 자식인 경우
        parent.left = child
    else:
        parent.right = child  # 노드가 부모노드의 오른쪽 자식인 경우
    return root


def delete_bst_case3(parent, root, node):  # 자식을 둘 가진놈을 삭제하는 경우
    succParent = node  # 후계자 노드의 부모노드
    succ = node.right  # 후계가 노드
    while succ.left is not None:  # 삭제하려는 노드의 오른쪽 서브 트리에서 가장 작은 노드를 찾기 위해서 왼쪽에 더이상 자식이 없을 때 가지 찾는다.
        succParent = succ  # 부모 노드하고 자리를 바꾼다.
        succ = succ.left

    if succ == succParent.left:
        succParent.left = succ.right
    else:
        succParent.right = succ.right

    node.key = succ.key
    node.value = node.value
    # node = succ
    return root


def delete_bst(root, key):
    if root == None:
        return None
    node = root
    parent = None
    while node is not None and node != key:
        parent = node
        if node.key > key:
            node = node.right
        else:
            node = node.left
    parent = None
    node = root
    while node != None and node.key != key:  # 반복문을 node가 빈노드가 아니거나 찾으려는 키값을 찾으면 관둔다
        parent = node  # 밑에서 node가 밑으로 이동할거기 때문에 부모노드를 미리 얻음
        if key < node.key:
            node = node.left
        else:
            node = node.right

    if node.left == None and node.right == None:
        delete_bst_case1(parent, root, node)
    elif node.left == None or node.right == None:
        delete_bst_case2(parent, root, node)
    else:
        delete_bst_case3(parent, root, node)


def combinDelete(root, key):

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

    if node is None:
        return None

    if node.left is None and node.right is None:

        def bst_dc1(root, node, parent):
            if parent is None:# 이거 틀림여
                root = None
            else:
                if node == parent.left:
                    parent.left = None#진은아 이거 여기서 None으로 안바꾸면 ㅈ된다.
                else:
                    parent.right = None
            return root

        bst_dc1(root, node,parent)


    elif node.left is None or node.right is None:

        def bst_dc2(root, node, parent):
            if node.left is not None:
                child = node.left
            else:
                child = node.right
            if root == node:
                root = child
            else:
                if parent.right == node:
                    parent.right = child
                else:
                    parent.left = child
            return root

        bst_dc2(root, node, parent)

    else:
        def delete_case_3(node, root, parent):
            succ = node.right
            succp = node

            while succ.left is not None:#이거 조심해 진은아 꼭 succ.left
                succp = succ
                succ = succ.left

            if succ == succp.left:
                succp.left = succ.right#진은아 이거 조심해 왼쪽으로 끝까지 갔으니까 오른쪽 자식이 있을 수가 없어
            else:
                succp.right = succ.right
            node.key = succ.key
            node.value = succ.value
            succ = node
            return root
        delete_case_3(node, root, parent)






def show_bst(root):
    if root is not None:
        show_bst(root.left)
        print(root.value, end=" ")
        show_bst(root.right)


a = Bnode(10, 'A')
b = Bnode(5, 'B')
c = Bnode(15, 'C')
d = Bnode(1, 'D')
e = Bnode(13, 'E')
f = Bnode(0, 'F')
g = Bnode(8, 'G')
h = Bnode(14, 'H')
list = [a, b, c, d, e, f, g, h]
for i in list:
    insert_bst(a, i)
show_bst(a)
list2 = [10, 1, 8]
for i in list2:
    combinDelete(a, i)
print()
show_bst(a)
