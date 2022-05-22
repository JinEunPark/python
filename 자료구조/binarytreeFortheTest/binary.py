from 자료구조.binarytreeFortheTest.Tnode import tnode

g = tnode('g')
h = tnode('h')
e = tnode('E')
d = tnode('D')
b = tnode('B')
a = tnode('A')
c = tnode('C')
f = tnode('F')
c.right = f
c.left = e
a.right = c
a.left = b
b.left = d
e.right = h
e.left = g

a1 = tnode('A')
a2 = tnode('B')
a3 = tnode('/')
a4 = tnode('*')
a5 = tnode('C')
a6 = tnode('*')
a7 = tnode('D')
a8 = tnode('+')
a9 = tnode('E')
a3.left = a1
a3.right = a2
a4.left = a3
a4.right = a5
a6.left = a4
a6.right = a7
a8.left = a6
a8.right = a9


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


inorder(a)
print()
preorder(a)
print()
inorder(a)
print()
inorder(a8)
print()
preorder(a8)
print()
postorder(a8)

c1 = tnode('1')
c2 = tnode('2')
c3 = tnode('3')
c1.right = c3
c1.left = c2


def is_complete_binarytree(root):
    list = []
    list.append(root)
    while len(list) > 0:

        node = list.pop(0)
        if node is not None and node.right != None and node.left == None:
            return False
        if node is not None:
            list.append(node.left)
            list.append(node.right)

    return True


def isCompleteBT(root):
    # Base Case: An empty tree is complete Binary tree
    if root is None:
        return True

    # Create an empty queue
    queue = []

    # Create a flag variable which will be set True
    # when a non-full node is seen
    flag = False

    # Do level order traversal using queue
    queue.append(root)
    while (len(queue) > 0):
        tempNode = queue.pop(0)  # Dequeue

        # Check if left child is present
        if (tempNode.left):

            # If we have seen a non-full node, and we see
            # a node with non-empty left child, then the
            # given tree is not a complete binary tree
            if flag == True:
                return False

            # Enqueue left child
            queue.append(tempNode.left)

            # If this a non-full node, set the flag as true
        else:
            flag = True

        # Check if right child is present
        if (tempNode.right):

            # If we have seen a non full node, and we
            # see a node with non-empty right child, then
            # the given tree is not a complete BT
            if flag == True:
                return False

            # Enqueue right child
            queue.append(tempNode.right)

        # If this is non-full node, set the flag as True
        else:
            flag = True

    # If we reach here, then the tree is complete BT
    return True

de = 0
def getLevel(root, node, depth):
    global de
    if node.data == root.data:
        de = depth
    elif node.data == root.data:
        de = depth
    if root is not None:
        if root.left is not None:
            getLevel(root.left, node, depth + 1)
        if root.right is not None:
            getLevel(root.right, node, depth + 1)



print(is_complete_binarytree(a))
print(is_complete_binarytree(a1))
print(isCompleteBT(a))

print(isCompleteBT(c1))

print(getLevel(a, g, 1))
print(de)