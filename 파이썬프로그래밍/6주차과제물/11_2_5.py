#11-2 실습 추가 5  - 사용자로부터 소문자로 입력받은 후 이르래 대문자 문자열로 변환하는 함수를 작성하시요
string = input("문자열을 입력하세요")
string2 =""
for i in string:
    string2 += chr(ord(i) - 32)
print(string2)
