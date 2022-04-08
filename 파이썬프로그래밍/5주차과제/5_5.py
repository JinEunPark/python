# 5
decimal = int(input("이 진수로 변환할 10 진수를 입력하세요"))
binary = ''
while True:
    if decimal == 0:
        break

    if decimal % 2 == 0:
        binary = '0' + binary
        decimal = decimal // 2
    else:
        binary = '1' + binary
        decimal = decimal // 2

print(binary)
