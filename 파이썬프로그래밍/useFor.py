# 반드시 존재해야 하는 것은 start값과 step 값이다
# start 와 step으 생략될 수 잇다. stop은 생략 될 수 없다:
#     step은 0 일 수 없다
# start 는 생략하면 0으로 처기화 되고 step은 생략하면 1로 초기화 된다.
for i in range(1, 9, 2):
    print(i)
for i in range(1, 9, 1):
    print(i)

n = int(input("정수를 입력하세요"))
sum = 0
step = 0
for i in range(0, n + 1):
    print(" %d: 현재의 i 값 " % i, end="")
    sum += i
print(sum, "총합")

for i in range(1, 0, 0):
    print(i, end="")
