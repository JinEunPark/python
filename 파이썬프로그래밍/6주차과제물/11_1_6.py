string = input("문자열을 입력하세요")
string2 = ''
index = 0
while True:
    string2 = string[index] + string2
    if index == len(string) - 1:
        break
    index += 1
if string == string2:
    print("회문구조 입니다")
else:
    print("회문구조가 아닙니다")
