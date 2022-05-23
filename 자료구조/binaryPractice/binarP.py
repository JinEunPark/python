from 자료구조.binaryPractice.Tnode import tnode

g = tnode('G')
h = tnode('H')
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


# 트리가 완전이진트리인지 판단하는 함수
def is_complete_binary_tree(root):
    list = []
    flag = False
    list.append(root)

    while len(list) > 0:
        node = list.pop(0)
        if node.left is not None:  # 왼쪽 자식이 있는데
            if flag == True:  # 위에서 자식이 하나 빈데가 있었어
                print("완전 이진트리가 아닙니다")
                return False
        else:
            flag = True
        if node.right is not None:  # 오른쪽 자식이 있는데
            if flag == True:  # 부모가 풀트리가 아니야
                print("완전 이진트리가 아닙니다")
                return False
        else:
            flag = True
        list.append(node.right)
        list.append(node.left)

    print("완전 이진트리 입니다")
    return True


# 트리를 뒤집는 함수
def revers(root):
    if root is not None:
        tmp = root.right
        root.right = root.left
        root.left = tmp
        revers(root.left)
        revers(root.right)


# 트리가 균형트리인지 아닌지 판단하는 함수
def is_balence(root):

    def cal_hight(node):
        if node is None:
            return 0
        if node is not None:
            lhight = is_balence(node.left)
            rhight = is_balence(node.right)

        if lhight > rhight:
            return lhight + 1
        else:
            return rhight + 1

    rhight = cal_hight(root.right)
    lhight = cal_hight(root.left)
    if abs(rhight - lhight) < 2:
        print("균형트리가 맞습니다.")


# 트리를 레벨순회로 출력하는 함수.
def levelRecursion(root):
    list = []
    list.append(root)
    while len(list) > 0:
        node = list.pop(0)
        if node is not None:
            print(node.data, end=" ")
            list.append(node.left)
            list.append(node.right)


# 트리의 해당노드의 레벨을 반환하는 함수
def getLevelOfTree(root, fnode):
    depth = 0

    def find(root, fnode, level):
        nonlocal depth
        if fnode == root:
            depth = level
        if root is not None:
            if root.left is not None:
                find(root.left, fnode, level + 1)
            if root.right is not None:
                find(root.right, fnode, level + 1)

        return depth

    getLevel = find(root, fnode, 1)
    return getLevel


is_complete_binary_tree(a)

list = [a, b, c, d, e, f, g, h]
count = 0

for i in list:
    count += 1
    print(count, "번째:", getLevelOfTree(a, i))
levelRecursion(a)
print()
revers(a)
levelRecursion(a)
is_balence(a)
dict = {"강아지": "dog", "고양이": "cat", "새": "bird"}
print(dict.keys())

dict = {"강아지": "dog", "고양이": "cat", "코끼리": "elephant", "bird": "새"}
while True:
    string = input("단어를 입력하세여")
    if string == '0':
        break
    else:
        if string in dict.keys():

            print(string, ":", dict[string])
        else:
            print("사전에 존재하지 않는 단어입니다 다시입력하세용")

file = open("/Users/bagjin-eun/Desktop/p/hello.txt", "w")  # w인 경우에는 오버라이트가 되어서 원래 존재하던 데이터가 사라진다.
file.write("hello world\n")
file.write("my name is park jin eun\n")
file.write("i just wanna girl firend who care about me and i will be your best friend so i willy miss you")
file.close()
print("파일을 찾아서 열어보세요")

file1 = open("/Users/bagjin-eun/Desktop/p/hello.txt", "w")
for i in range(1, 10):
    file1.write("5 x %d = %d\n" % (i, i * 5))
file1.close()