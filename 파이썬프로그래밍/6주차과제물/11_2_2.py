num = int(input("자연수를 입력하세요"))
factorial = 1
for i in range(1,num+1):
    factorial *= i
print(" %d 팩토리얼의 값: %d" %(num,factorial))
