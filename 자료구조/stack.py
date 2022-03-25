class stack:
    def __init__(self):
        self.top = []

    def isEmpty(self):
        return len(self.top) == 0

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if len(self.top) != 0:
            return self.top.pop(-1)  # -1 대신에 length of top 에 -1도 가능합니다.

    def peek(self):
        if len(self.top) != 0:
            return self.top[-1]

    def display(self):
        print(self.top)

    def __sizeof__(self):
        return len(self.pop)

    def __str__(self):
        return str(self.top)


# Astack = stack()
# for i in range(0, 6):
#     Astack.push(i)
#
# print("push 5 times", Astack.top)
# print("result of top", Astack.pop())
# print("after pop ", Astack.top)
#
# odd = stack()
# even = stack()
#
# for i in range(100):
#     if i % 2 == 0:
#         odd.push(i)
#     else:
#         even.push(i)
# print(odd)
# print(even)
#
# for _ in range(10):
#     odd.pop()
#     even.pop()
#
# print(odd)
# print(even)
#
#
# def checkBrackets(statement):
#     check = stack()
#     for ch in statement:
#         if ch in ['(', '{', '[']:
#             check.push(ch)
#         elif ch in [')', '}', ']']:
#             if check.isEmpty():
#                 return False
#             else:
#                 left = check.pop()
#                 if (ch == ")" and left != "(") or \
#                         (ch == "}" and left != "{") or \
#                         (ch == "]" and left != "["):
#                     return False
#
#     return check.isEmpty()
#
#
# statement = input("rhkgy")
# print(checkBrackets(statement))


def evalPostfix(expr):
    s = stack()
    for token in expr:
        if token in '+-/*':
            val2 = s.pop()
            val1 = s.pop()
            if token == '+':
                s.push(val1 + val2)
            elif token == '*':
                s.push(val1 * val2)
            elif token == '-':
                s.push(val1 - val2)
            elif token == '/':
                s.push(val1 / val2)
            elif token == '%':
                s.push(val1 % val2)
        else:
            s.push(float(token))

    return s.pop()


def precedence(op):
    if op in '()':
        return 0
    elif op in '+-':
        return 1
    elif op in '*/':
        return 2
    else:
        return -1


def Infix2Postfix(expr):  # 입력값 리스트
    s = stack()
    output = []

    for term in expr:
        if term == '(':  # 왼쪽괄호라면바로스택에 추가
            s.push(term)
        elif term == ')':  # 오른쪽 괄호를 만나면 그동안 스택에 들어있던 연산자 모두 출력
            while not s.isEmpty():
                op = s.pop()
                if op == '(':  # 왼쪽괄호가 나오면 출력중지
                    break
                else:
                    output.append(op)  # 왼쪽괄호가 아니며 전부 리스트 뒤로 추가
        elif term in '+-/*':  # 연산자이면
            while not s.isEmpty():
                op = s.peek()  # 스택에서 객체를 참조하고 삭제하지 않는 메소드
                if (precedence(term) <= precedence(op)):  # 우선순위가 높거나 같은 연산자들을 모두 출력
                    output.append(op)  # 우선순위가 같아도 출력하는 이유는 같은 우선순위에서도 출력하지 않으면 계산순서가 뒤바뀐다.
                    s.pop()  # 스택에서 객체를 반환하고 스택에서 삭제하는 메소드
                else:
                    break
            s.push(term)  # 연산자가 아니면 객체에 색입
        else:
            output.append(term)

    while not s.isEmpty():
        output.append(s.pop())

    return output


expr = input("중위표기 수식을 공백을 기준으로 입력하세요")
expr = expr.split()#공백을 기준으로 문자열을 잘라서 리스트 생성후 다시 반환
postfix = Infix2Postfix(expr)
print(evalPostfix(postfix))
#
# print(evalPostfix(POSTFIX))
