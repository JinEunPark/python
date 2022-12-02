# Radix sort in Python


# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array) #배열 사이즈를 가져옴
    output = [0] * size # 정렬하려는 배열과 같은 사이즈의 배열을 생성함
    count = [0] * 10 #길이가 총 10인 배열을 생성함

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place #자릿수로 나눈 몫을 인덱스로 사용 만약 123이면 10의 자리수라 하면 인덱스에 12
        count[index % 10] += 1 #인덱스에 10나머지 연산을 적용해서 12중 2만 추출함

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1] #counting sort과정 개별리스트의 합 배열을 만듬

    # Place the elements in sorted order
    i = size - 1 #원본 배열을 한바퀴 돌기 위해서 실행
    while i >= 0:
        index = array[i] // place #지리수로 거르기 위한 연산
        output[count[index % 10] - 1] = array[i] #count[index % 10] - 1 -> 원본 배열의 숫자의 갯수 -1  이 새로운 배열의 인덱스임
        count[index % 10] -= 1# 새로운 배열에 삽입하면 갯수를 하나 감소시킴
        i -= 1# 뒤에서 부터 삽입이 끝나면 인덱스를 하나 감소시킴

    for i in range(0, size): #새로 만든 배열을 원본에다가 복사함
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array) #최대자리수를 알아내기 위해서 가장 큰 수를 알아냄

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:#가장 큰 수의 자릿수를 넘어가면 중단됨
        countingSort(array, place)# counting sorting 호출함
        place *= 10


data = [121, 432, 564, 23, 1, 45, 788]
radixSort(data)
print(data)
