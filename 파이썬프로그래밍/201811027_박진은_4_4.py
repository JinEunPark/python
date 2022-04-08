# 1번
sum = 0
while True:
    e = int(input("더하려는 양의 정수를 입력하세요"))
    if e == 0:
        break
    sum += e
print("숫자들의 총합은 ", sum, "입니다")

# 2번
n = int(input("정수를입력하세요"))
sum2 = 0
while n > 0:
    if n % 2 == 0:
        sum2 += n
    n -= 1
print("1 부터 n 까지의 짝수들의 합은 ", sum2, "입니다")

# 3번


factorial = int(input("정수 n 입력하세요"))
result = 1
if factorial != 1:
    while factorial > 0:
        result *= factorial
        factorial -= 1
    print("factorial of n :", result)
else:
    print("factorial:0")
# 5
decimal = int(input("이 진수로 변환할 10 진수를 입력하세요"))
binary = ''
while True:
    if decimal == 0:
        break

    if decimal % 2 == 0:
        binary = '0' + binary
        decimal = decimal // 2
    else:
        binary = '1' + binary
        decimal = decimal // 2

print(binary)

# 4
str = input("문자열을 입력하세요")
lenght = len(str) - 1
while lenght >= 0:
    print(str[lenght], end="")
    lenght += -1
