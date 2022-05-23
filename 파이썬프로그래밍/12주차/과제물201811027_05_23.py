movie_dict = {}
file = open("movie_data.txt", "r", encoding='cp949')
# 제목 보급사 개봉일 국가 상영과수 수입 전체관객 수 등급   0   
for line in file.readlines():
    line = line.strip()
    datalist = line.split("|")
    movie_dict[datalist[2]] = [datalist[3], datalist[4], datalist[5], datalist[6], datalist[7], datalist[8],
                               datalist[9]]
print(movie_dict)
list = ["company", "Release date", "Total screen", "Profit", "Total num", "Grade"]
while True:
    f_value = input("찾으시는 영화를 입력하세요")
    if f_value == "0":
        print("프로그램을 종료합니다")
        break

    if f_value in movie_dict.keys():
        data = movie_dict[f_value]
        for i in range(0, 6):
            print("%s : %s" % (list[i], data[i]))
        print("---------------------------------------------")
    else:
        print("찾으시는 영화가 존재하지 않습니다.")
