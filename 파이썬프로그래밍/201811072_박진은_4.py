# 1
score = int(input("학점을 입력하세요"))
if score > 140:
    print("졸업가능")
else:
    print("졸업불가능")


#2
height = int(input("키를 입력하세요"))
age = int(input("나이를 입력하세요"))


if height > 140 and age < 19:
    print("탑승가능")
else:
    print("탑승불가능")


# 3
apple = int(input("구매할 사과의 갯수를 입력하세요"))
grape = int(input("구매할 포도의 갯수를 입력하세요"))
pear = int(input("구매할 배의 갯수를 입력하세요"))
tengerin = int(input("구매할 귤의 갯수를 입력하세요"))
sum = apple * 1000 + grape * 3000 + pear * 2000 + tengerin * 500

if grape > 3:
    sum = 0.9 * sum
    print(sum, "가격이 할인됨")
else:
    print(sum, "할인이 적용되지 않음")

# 4
bankName = input("은행이름을 입력하세요")
way = input("입급 수단을 방법을 입력하세요")
money_check = input(" 입금하실 돈을 입력하세요")

if bankName == "파이" and (way == "card" or way == "bankbook") and (money_check == "money"):
    print("입급 가능")
else:
    print("입급불가능")


# 5
finger = int(input(" 손가락의 둘레를 입력하세요"))

if finger >= 51 and finger < 55:

    if finger > 51 and finger <= 52:
        print("9호 반지를 제작하세요")
    elif finger > 52 and finger <= 53:
        print("10호 반지를 제작하세요")

    elif finger > 53 and finger <= 54:
        print("11호 반지를 제작하세요")

    elif finger > 54 and finger <= 55:
        print("12호 반지를 제작하세요")

else:
    print("반지의 제작이 불가능합니다")

# 6
calcul = input("덧샘 1, 뺄셈 2, 곱셈3, 나눗셈4")
a = int(input("연산할 양의 정수를 입력하세요"))
b = int(input("연산할 양의 정수를 입력하세요"))

if calcul in '1,2,3,4':
    if calcul == '1':
        print("덧셈의 결과:", a + b)
    elif calcul == '2':
        print("뺄셈의 결과:", a - b)
    elif calcul == '3':
        print("곱셈의 결과:", a * b)
    elif calcul == '4':
        print("나눗셈의 결과:", a / b)

else:
    print("올바른 연산자 번호를 입력하세요")


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


# 9
a = int(input("첫번째 변의 길이를 입력하세요"))
b = int(input("두번째 변의 길이를 입력하세요"))
c = int(input("세번째 변의 길이를 입력하세요"))
most = 0
mid = 0
small = 0

if a > b:
    if a > c:
        most = a
        if b > c:
            mid = b
            small = c
        else:
            mid = c
            small = b
    else:
        most = c
        if a > b:
            mid = a
            small = b
        else:
            mid = b
            small = a
else:
    if b > c:
        most = b
        if a > c:
            mid = a
            small = c
        else:
            mid = c
            small = a
    else:
        most = c
        if a > b:
            mid = a
            small = b
        else:
            mid = b
            small = a


print(most,mid,small)


if most > mid+small:
    print("삼각형이 불가능합니다")

else:
    if most == mid and mid  == small:
        print("정삼각형입니다")
    elif most**2 == mid **2 + small**2:
        print("직각삼각형입니다.")
    elif most==mid or mid == small:
        print("이등변삼각형입니다.")
    else:
        print("일반삼각형입나다")