list = []
print("=======좋아하는 과일 등록하는 방법=======")
while True:
    f = input("좋아하는 과일을 입력하세요")
    if f == "0":
        break
    list.append(f)
print("좋아하는 과일: ",list)