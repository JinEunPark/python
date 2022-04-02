from Stack_p import stack


class computeBackToForward(stack):

    def __init__(self):
        super(computeBackToForward, self)

    def evalpostfix(self, string):
        s = stack()
        for i in string:
            if i in '+/-*':
                value2 = s.pop()
                value1 = s.pop()
                if i == '+':
                    s.push(value1 + value2)
                elif i == '-':
                    s.push(value1 - value2)  # 먼저 나온게 뺄샘을 당한다.
                elif i == '/':
                    s.push(value1 / value2)  # 먼저 나온게 분자가 된다.

                elif i == '*':
                    s.push(value1 * value2)
            else:
                s.push(float(i))
        return s.pop()

    def preference(self, cha):
        if cha == ')}]':
            return 0

        elif cha in '+-':
            return 1
        elif cha == '*/':
            return 0

    def prefixpost(self, string):
        out = []
        s = stack()
        for term in string:
            if term == '(':
                s.push(term)#괄호 나오면 바로 스텍에 ㄱ

            elif term == ')':# 오른쪽 괄호 나오면 바로 스택안에 있는 연산자 다 꺼내서 out 에 넣어
                s.push(')')
                while s.isEmpty():
                    e = s.peek
                    if e == ')':
                        break
                    else:
                        out.append(e)

            elif term in '+-*/':
                while s.isEmpty():
                    e = s.peek()
                    if self.preference(term) <= self.preference(e):
                        out.append(e)
                        s.pop()
                    else:
                        break
                    s.push(term)

