# 1번
sum = 0
while True:
    e = int(input("더하려는 양의 정수를 입력하세요"))
    if e == 0:
        break
    sum += e
print("숫자들의 총합은 ", sum, "입니다")