# 3
apple = int(input("구매할 사과의 갯수를 입력하세요"))
grape = int(input("구매할 포도의 갯수를 입력하세요"))
pear = int(input("구매할 배의 갯수를 입력하세요"))
tengerin = int(input("구매할 귤의 갯수를 입력하세요"))
sum = apple * 1000 + grape * 3000 + pear * 2000 + tengerin * 500

if grape > 3:
    sum = 0.9 * sum
    print(sum, "가격이 할인됨")
else:
    print(sum, "할인이 적용되지 않음")
