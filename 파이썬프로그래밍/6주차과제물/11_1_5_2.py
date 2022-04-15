# 이진수를 문자열로 입력받아서 10 진수로 출력하는 프러그램을 작성하시오
binary = input("이진수를 입력하세요")
result = 0
i = len(binary) - 1
while i >= 0:
    if binary[len(binary) - 1 - i] == '1':
        result += 2 ** i
    else:
        continue
    i -= 1

print(result)
