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
