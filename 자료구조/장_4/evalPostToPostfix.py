from 자료구조.장_4.stack import stack


def precedence(n):
    if n in "()":
        return 0
    elif n in '+-':
        return 1
    elif n in '/*':
        return 2
    else:
        return -1


def evalToPost(string):
    s = stack()
    output = []
    for token in string:
        if token == "(":
            s.push("(")
        elif token == ")":
            while not s.isEmpty():  # 진은아 아까 너 이거 틀렸어 시험전에 다시 봐봐
                # 너는 아까 while True 이렇게 만들었었어
                cal = s.pop()
                if cal == "(":
                    break
                output.append(cal)
        elif token in '+-/*':
            while not s.isEmpty():
                cal = s.peek()
                if precedence(cal) >= precedence(token):
                    output.append(cal)
                else:
                    break
            s.push(token)  # 마지막으로 현재 연산자 넣는거 까먹지 말자 진은아

        #     cal = s.peek()
        #
        # while precedence(token) <= precedence(cal):
        #     output.append(cal)
        #     cal = s.pop()
        else:
            output.append(token) # 피연산이면 묻지도 따지지도 않고 바로 출력 조지는겁닌다 아시겠어요?
            


    while s.isempty():
        output.append(s.pop())

    return output


