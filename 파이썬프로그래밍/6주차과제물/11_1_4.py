string = input("문자열을입력하세요")
string2 = ""
count = 0
while True:
    string2 = string[count] + string2
    count +=1
    if count == len(string):
        break
print("revers string 2 :" , string2)