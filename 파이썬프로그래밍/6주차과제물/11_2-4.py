string = input("문자열 입력하세요")
string2 = ""
for i in string:
    string2 = i + string2
if string == string2:
    print("회문구조")
else:
    print("회문구조가 아닙니다.")
