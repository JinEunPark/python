list_E = []
list_M = []
list_K = []
sumk = 0
sume = 0
summ= 0
for i in range(3):
    print(i+1,"번째 학생")
    list_K.append(int(input("국어 성적을 입력하세요")))
    list_E.append(int(input("영어 성적을 입력하세요")))
    list_M.append(int(input("수학 성적을 입력하세요")))
    sumk+=list_K[i]
    sume+=list_E[i]
    summ+=list_M[i]


print("번호 국어 영어 수학")

for i in range(3):
    print("{0:d} {1:5d} {2:5d} {3:5d}".format(i+1,list_K[i],list_E[i],list_M[i]))
print("----------------------")
print("평균 {0:4.2f} {1:3.2f} {2:3.2f}".format(sumk/3,sume/3,summ/3))



