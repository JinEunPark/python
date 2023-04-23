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

print(most, mid, small)

if most > mid + small:
    print("삼각형이 불가능합니다")

else:
    if most == mid and mid == small:
        print("정삼각형입니다")
    elif most ** 2 == mid ** 2 + small ** 2:
        print("직각삼각형입니다.")
    elif most == mid or mid == small:
        print("이등변삼각형입니다.")
    else:
        print("일반삼각형입나다")
