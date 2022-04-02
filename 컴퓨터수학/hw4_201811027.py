money = 10000
sum = 10000 # 첫날은 넣어 두었다고 가정

sum = sum * (1.03**10)
print(sum)

sum1 = 0
for i in range(20):
    sum1 += money
    sum1 = sum1 * 1.03
print(sum1)
