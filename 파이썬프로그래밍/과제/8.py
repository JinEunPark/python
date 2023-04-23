# 8
value = int(input("첫번째  정수를 입력하세요"))
value2 = int(input("두번째 정수를 입렬하세요"))
value3 = int(input("세번째 정수를 입렬하세요"))
sum = value + value2 + value3

if sum % 2 == 0:
    if value > value2:
        if value > value3:
            print("가장 큰 수는 ", value)
        else:
            print("가장 큰 수는 ", value3)
    else:
        if value2 > value3:
            print("가장 큰 수는 ", value2)
        else:
            print("가장 큰 수는 ", value3)
else:
    print(" 모든 정수의 합은: ", sum)
