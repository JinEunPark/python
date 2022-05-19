from 자료구조.BST.BSTnode import bstnode

a = bstnode(18, 'A')
b = bstnode(7, 'B')
c = bstnode(3, 'C')
d = bstnode(12, 'D')
e = bstnode(26, 'E')
f = bstnode(31, 'F')
g = bstnode(27, 'G')

a.left = b
a.right = e
b.left = c
b.right = d
e.right = f
f.left = g


def findmax_bst(node):
    if node != None:
        if node.right == None:
            return node
        else:
            return findmax_bst(node.right)


def findmin_bst(node):
    if node != None:
        if node.left == None:
            return node
        else:
            return findmin_bst(node.left)


result = findmax_bst(a)
print(result.value, result.key)
result2 = findmin_bst(a)
print(result2.value, result2.key)



def insert_bst_repeat(compareNode, newNode):

    while(True):

        if newNode.key < compareNode.key:
            if compareNode.left == None:
                compareNode.left = newNode
                return True

            else:
                compareNode = compareNode.left
                # return insert_bst(compareNode.left, newNode)
        elif newNode.key > compareNode.key:
            if compareNode.right == None:
                compareNode.right = newNode
                return True

            else:
                compareNode = compareNode.right
                # return insert_bst(compareNode.right, newNode)
        elif newNode.key == compareNode.key:
            return False

def showBST(node):

    if node is not None:
        showBST(node.left)
        print(node.key,end='  ')
        showBST(node.right)


showBST(a)
print()
newNode = bstnode(9,'H')
insert_bst_repeat(a,newNode)
showBST(a)



