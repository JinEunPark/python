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
