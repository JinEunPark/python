def sum(a, b):
    return a + b


def minus(a, b):
    if a < b:
        return b - a
    else:
        return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


while True:
    print("======계산기=======")
    answer = int(input("1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 5.종료:"))
    if answer == 5:
        print("프로그램을 종료합니다.")
        break
        print("두개의 정수를 입력하세요")
    a = float(input())
    b = float(input())

    if answer == 1:
        print("결과:", sum(a, b))
    elif answer == 2:
        print("결과:", minus(a, b))
    elif answer == 3:
        print("결과:", mul(a, b))
    elif answer == 4:
        print("결과:", div(a, b))
