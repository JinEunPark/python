list_score = []
sum = 0
for i in range(5):
    print("{}번 학생의 성적:".format(i+1),end='')
    list_score.append(int(input()))
    sum += list_score[i]

print("성적합계:",sum)
print("성적평균:",sum/5)