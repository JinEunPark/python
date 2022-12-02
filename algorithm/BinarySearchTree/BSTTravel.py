from algorithm.BinarySearchTree.Node import Node

d = Node('D', None, None)
e = Node('E', None, None)
f = Node('F', None, None)
b = Node('B', d, e)
c = Node('C', f, None)
a = Node('A', b, c)

def preOrder(node): #전위표기법 가우네 왼쪽 오른쪽
    if node is not None:
        print(node.data, end=' ')
        preOrder(node.left)
        preOrder(node.right)

def inOrder(node): # 중위 표기법 왼쪽 가운데 오른쪽
    if node is not None:
        inOrder(node.left)
        print(node.data, end=' ')
        inOrder(node.right)

def postOrder(node): # 후위표기법 왼쪽 오른쪽 가운데
    if node is not None:
        postOrder(node.left)
        postOrder(node.right)
        print(node.data, end=' ')


preOrder(a)
print()
postOrder(a)
print()
inOrder(a)




