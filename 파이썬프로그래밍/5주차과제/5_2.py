# 2번
n = int(input("정수를입력하세요"))
sum2 = 0
while n > 0:
    if n % 2 == 0:
        sum2 += n
    n -= 1
print("1 부터 n 까지의 짝수들의 합은 ", sum2, "입니다")