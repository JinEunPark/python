# 이진수를 문자열로 입력받아서 10 진수로 출력하는 프러그램을 작성하시오
binary = input("이진수를 입력하세요")
i = 0
result = 0
for i in range(len(binary)-1, -1, -1):
    if binary[(len(binary)-1)-i] == '1':
        result += 2 **i
    else:
        continue
print(result)


