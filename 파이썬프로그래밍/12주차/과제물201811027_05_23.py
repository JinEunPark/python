dict = {"강아지": "dog", "고양이": "cat", "코끼리": "elephant", "bird": "새"}
while True:
    string = input("단어를 입력하세여")
    if string == '0':
        break
    else:
        if string in dict.keys():

            print(string, ":", dict[string])
        else:
            print("사전에 존재하지 않는 단어입니다 다시입력하세용")