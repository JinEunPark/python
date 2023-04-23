# 7
x = int(input("첫 번째 정수를 입력하세요"))
y = int(input("둘 번째 정수를 입력하세요"))
z = int(input("셋 번째 정수를 입력하세요"))

if x > y:

    if x > z:
        print("가장 큰 수는 ", x)
    else:
        print("가장 큰 수는 ", z)
else:
    if y > z:
        print("가장 큰 수는 ", y)
    else:
        print("가장 큰 수는 ", z)
