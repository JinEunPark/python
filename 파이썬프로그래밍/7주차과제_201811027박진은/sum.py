# 섭씨온도를 입력받아 화씨온도로 변환해 알려주는 프로그램을 작성하시오. (소수점 2자리, 화씨 = 섭씨 * (9/5) + 32)
print("===섭씨 화씨 온도 계산기===")
celsius = float(input("섭씨온도를 입력하세요"))
fahrenheit = celsius * (9 / 5) + 32
print("섭씨 :%.2f \n화씨 :%.2f" % (celsius, fahrenheit))

print("===섭씨 화씨 온도 계산기===")
celsius = float(input("섭씨온도를 입력하세요"))
fahrenheit = celsius * (9 / 5) + 32
print("섭씨 {0:.2f} \n화씨 {1:.2f}".format(celsius, fahrenheit))

# 저축액을 입력받아 1년 후의 원금, 이자, 세금, 최종금액을 출력하는 프로그램을 작성하시오.

print("===원리금 합계 프로그램===")
initial = int(input("원금을 입력하세요"))
interest = initial * 0.0375
tax = interest * 0.15
result = initial + interest - tax
print("원금 :{0:.0f}\n이자:{1:.0f}\n세금:{2:.0f}\n최종:{3:.0f}".format(initial, interest, tax, result))

print("===원리금 합계 프로그램===")
initial = int(input("원금을 입력하세요"))
interest = initial * 0.0375
tax = interest * 0.15
result = initial + interest - tax
print("원금:%.0f\n이자:%.0f\n세금:%.0f\n최종:%.0f" % (initial, interest, tax, result))

# 3) 두 정수를 입력받아 사칙연산 결과를 열을 맞추어 출력해주는 프로그램을 작성하시오.
a = int(input("첫번째 정수를 입력하세요"))
b = int(input("두번쩨 정수를 입력하세요"))
print("{:15.2f} + {:15.2f} = {:15.2f}".format(a, b, a + b))
print("{:15.2f} - {:15.2f} = {:15.2f}".format(a, b, a - b))
print("{:15.2f} * {:15.2f} = {:15.2f}".format(a, b, a * b))
print("{:15.2f} / {:15.2f} = {:15.2f}".format(a, b, a / b))

# 4) 두 실수를 입력받아 사칙연산 결과를 열을 맞추어 출력해주는 프로그램을 작성하시오. (단, 모든 수치는 소수점 둘째 자리까지 표시하시오)
