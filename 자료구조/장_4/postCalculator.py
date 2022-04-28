from 자료구조.장_4.stack import stack


def postCalculator(string):
    s = stack()

    for i in string:
        if i in '*+/-':
            value2 = s.pop()
            value1 = s.pop()
            if i == '*':
                s.push(value1 * value2)
            if i == '+':
                s.push(value1 + value2)
            if i == '-':
                s.push(value1 - value2)
            if i == '/':
                s.push(value1 / value2)
        else:
            s.push(float(i))#진은아 이거 까먹으면 존나 골치아파진다
    return s.pop()


print(postCalculator("38*3-7/"))
