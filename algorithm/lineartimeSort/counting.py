number_list = [1,5,3,1,4,2,5,2,1,5,7,7,5,4,6,7,8,9,8,5,4,3,2,6,5,4,5,6,2,1,3,10]
print(len(number_list))
count = [0 for i in range(0,10)]#갯수를 세어서 반환할 것
new_list = [0 for i in range(len(number_list))]#위와 동일한 길이의 배열을 만듬 반환할 배열

for i in number_list: #원본을 순회하면서 값보다 하나 작은 수를 인덱스로 해서 count 배열을 증가 시킴
    count[i-1]+=1
print(count)
for i in range(len(count)):#반복문을 순회하면서 전에 있던 수를 앞에 있던 수와 합침
    if i != 0:
        count[i] = count[i-1] + count[i]
print(count)

for i in range(len(number_list)):#원본 배열안에 들어있는 값보다 하나 작은 값이 count배열에 인덱스임 count배열에 들어있는 값보다 하나 작은 값이
    #새로 생기는 배열의 인덱스임
    #새로 생기는 배열[count[원래 배열에 -1한값]-1] = 원래 배열의 값을 넣음
    new_list[count[number_list[i]-1]-1] = number_list[i]
    count[number_list[i]-1] += -1



print(new_list)