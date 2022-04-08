factorial = int(input("정수 n 입력하세요"))
result = 1
if factorial != 1:
    while factorial > 0:
        result *= factorial
        factorial -= 1
    print("factorial of n :", result)
else:
    print("factorial:0")