from 자료구조.poststack.stack import stack


def evalPostFix(string):
    s = stack()
    for i in string:
        if i in '+-/*':
            value2 = s.pop()
            value1 = s.pop()
            if i == '+':
                s.push(value1 + value2)
            if i == '-':
                s.push(value1 - value2)
            if i == '/':
                s.push(value1 / value2)
            if i == '*':
                s.push(value1 * value2)# 진은아 연산하나도 안빼 놓고 조져야ㅇ해
        else:
            s.push(float(i))
    return s.pop()


string = ['8', '2', '/', '3', '-', '3', '2', '*', '+']
print(evalPostFix(string))
