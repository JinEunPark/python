from 자료구조.poststack.evalPostFix import evalPostFix
from 자료구조.poststack.stack import stack


def precedence(string):  # 우선순위가 높을 수록 높은 숫자로 처리하고 괄호는 가장 낮은 우선순위를 가진것으로 처리한디.
    if (string == '(') or (string == ')'):
        return 0
    elif (string == '+') or (string == '-'):
        return 1
    elif (string == '/') or (string == '*'):
        return 2
    else:
        return -1


def infixToPostfix(string):
    s = stack()
    output = []
    for i in string:

        if i == '(':
            s.push('(')

        elif i == ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)

        elif i in '+-/*':

            while not s.isEmpty():
                before = s.peek()  # 제발 진은아 이 시발로마 괄호좀 붙여
                if precedence(i) <= precedence(before):
                    output.append(before)
                    s.pop()
                else:
                    break
            s.push(i)

        else:
            output.append(i)

    while not s.isEmpty():
        output.append(s.pop())

        return output



str = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']


print(infixToPostfix(str))
print(evalPostFix(infixToPostfix(str)))
