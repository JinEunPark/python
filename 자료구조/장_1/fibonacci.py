def fibocursion(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return fibocursion(n - 1) + fibocursion(n - 2)


print(fibocursion(3))


def fibo(n):
    if n < 2:
        return n
    else:
        past = 0
        current = 1
        for i in range(2, n + 1): # 피보나치 수열에서 이미 past하고 current를 지정했으니까 2 번째 까지는 한거랑 마친가지 인거야 진은아
            tmp = current  # n-1 번째 값을 저장
            current += past  # n-1 번째 더하기 n -2를 해서 current 를  n 번째로 만든다 다음 반복문에는 curent 는 n - 1이 된다.
            past = tmp  # n - 2 번째를 n-1 번째로 옮긴다
        return current


print(fibo(3))
