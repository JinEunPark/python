import random

answer = int(random.random()*100)


tmp = 0
max = 100
min = 0

while True:
    n = int(input("숫자를 입력하세요"))
    if n < answer:
        min = n
        print("더 큰 수를 압력하세요(범위 {} ~ {})".format(min, max))
        tmp += 1
    elif n > answer:
        max = n
        print("더 작은 수를 입력하세요(범위 {} ~ {})".format(min, max))
        tmp += 1
    elif n == answer:
        print("게임 성공")
        break
    if tmp > 10:
        print("시도 횟수 초과 게임 실패 게임을 계속하시겠습니까 y/n")
        chioce = input()
        if chioce == 'y':
            answer = int(random.random() % 100)
            continue
        else:
            break

print("게임 종료")
