


def bucketSort(array):

    bucket = []

    for i in range(len(array)):
        bucket.append([]) #원본 배열의 길이 만큼 삽입해서 구현

    for j in array:

        index_b = int(10*j)
        #array안에 소수점이 들어있다고 가정하기
        # 때문에 이에 10을 곱하고 int() 메소드를 통해 내림해서 인덱스로 만듬

        bucket[index_b].append(j)#소수점 첫번째 자리에 삽입

    for i in range(len(array)):
        insertionSort(bucket[i]) #각각에 bucket에 해당하는것을 구현함

    k = 0 #새로운 인덱스

    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]#이미 정렬된 것들을 차래대로 삽입함
            k+=1


    return array

def insertionSort(array):

    for i in range(len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j-1

        array[j+1] = key
array = [.42, .32, .33, .52, .37, .47, .51]


print(bucketSort(array))

