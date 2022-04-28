from 자료구조.poststack.stack import stack  # 경로 명을 다 써줘야 하나봐 진은아


def checkbrakets(string):
    s = stack()
    for i in string:
        if i in '[{(':
            s.push(i)
        elif i in ']})':
            if s.isEmpty():  # 조건 2에 위반됨 오른쪽 괄호가 왼쪽 괄호보다 먼저 나와야 한다
                return False
            else:
                left = s.pop()
                if (i == ']' and left != '[') or (i == '}' and left != '{') or (i == ')' and left != '('):
                    return False
    return s.isEmpty()  # 반목문이 끝난 후 위조건에 걸리지 않고 모든 괄호이 수가 맞아서 스택이 비워있으면 조건 1 괄호의 갯수가 같아야 하는 것도 만족하는 거임


string = '{snklnflsnefs[aejnsejf]s efkj()[ss}'
print(checkbrakets(string))
