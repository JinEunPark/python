def is_prime():
    n = int(input("정수를입력하세요"))
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(n, "은 소수 입니다")
    else:
        print("소수가 아닙니다")
is_prime()