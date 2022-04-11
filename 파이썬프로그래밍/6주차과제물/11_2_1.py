num = int(input("정수를 입력하세요"))
sum = 0
for i in range(num+1):
    if i%2 == 0:
        sum += i
    else:
        continue
print("짝수들의 합은 %d" %sum)