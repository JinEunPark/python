print("친구이름 등록 프로그램")
print("0을 입력하면 프로그램 종료")
list_friend = []
while True:
    friend = input("친구이름을 입력하세요")
    if friend == "0":
        print("등록이 완료 되었습니다")
        break
    list_friend.append(friend)
print("입력된 순서: ",list_friend)
list_friend.sort()
print("정렬된 순서: ",list_friend)
