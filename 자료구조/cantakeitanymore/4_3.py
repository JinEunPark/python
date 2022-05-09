import classStack


def checkPy():
    s = classStack.stack()
    filename = input("파이썬 파일의 경로를 입력하세요")
    file = open(filename, "r")
    data = 0
    row = 0
    while data != None:
        row += 1
        data = file.readline()
        for i in data:
            if i in '({[':
                s.push(i)
            elif i in ')}]':
                cha = s.pop()

                if i == ')' and cha == '(' or i == '}' and cha == '{' or i == ']' and cha == '[':
                    continue
                elif i in ')]}' and cha in ')}]':
                    print("행:{} 열 {}".format(row, i))
                    return 2
                elif i == ')' and cha in '{[' or i == '}' and cha in '[(' or i == ']' and cha in '})':
                    print("행:{} 열 {}".format(row, i))
                    return 3
        if s.__sizeof__() != 0:
            print("행:{} 열 {}".format(row, i))
            return 1
    return 0


print(checkPy())
