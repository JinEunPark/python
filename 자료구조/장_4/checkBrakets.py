from 자료구조.장_4.stack import stack


def checkBrakets(string):
    s = stack()
    for i in string:
        if i in '{[(':
            s.push(i)
        elif i in '}])':
            if s.isEmpty():
                return False
            else:
                left = s.pop()

                if (left == '{' and i == '}') or (left == '[' and i == ']') or (left == '(' and i == ')'):
                    continue
                else:
                    return False
    return s.isEmpty()

print(checkBrakets("(dfnjgaer.kjngaerg[aerghbalehrblger]a.jehrflhar{s.ejrbgjkaebrg}"))