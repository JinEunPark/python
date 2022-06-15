need_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

sorted = [35, 4, 6245, 62, 442, 341, 35, 255, 2, 3]#정렬될 원소들이 임시로 저장되어질 함수


def merge(list, left, mid, right):#병합을 진행하는 함수

    global sorted#전역변수 사용설정

    leftIndex = left #왼쪽 리스트의 첫번째 원소를 가르키는 리스트
    sortedIndex = left#정렬될 원소들이 들어갈 리스트를 현재 함수에서 가장 작은 left로 초기화해서 사용한다.
    rightIndex = mid + 1#오른쪽 리스트의 가장 첫번째 원소를 가르키기 위해서 mid +1을 사용함

    while leftIndex <= mid and rightIndex <= right:#둘다 반으로 나눈 범위를 넘지안을때 까지 실행함.
        if list[leftIndex] <= list[rightIndex]:#만일 왼쪽 리스트의 값이 오른쪽 리스트 보다 작다면
            sorted[sortedIndex] = list[leftIndex]#왼쪽 리스트의 값을 정렬된 리스트에 추가하고
            sortedIndex, leftIndex = sortedIndex + 1, leftIndex + 1#왼쪽 그리고 정렬된 리스트의 인덱스의 값을 증가시킴
        else:
            sorted[sortedIndex] = list[rightIndex]# 오늘쪽 리스트의 값이 더 작으면 정렬된 리스트에 오른쪽 값을 삽입한다.
            sortedIndex, rightIndex = sortedIndex + 1, rightIndex + 1#오르쪽 인덱스와 정렬된 리스트의 값을 증가

    if left > mid:#왼쪽이 mid보다 크다는거는 오른쪽리스트 보다 작은 값이 많아서 이미 정렬된 리스트에 다 들어갔다는 거임
        #오른쪽 리스트에 남은 값들을 정렬된 리스트에 삽입한다.
        sorted[sortedIndex: sortedIndex + right - rightIndex + 1] = list[rightIndex:right]#오른쪽 인덱스부터 끝까지
        #리스트에 삽입된 인덱스부터 right - rightIndex:오른쪽에 남은 인덱스 만큼

    else:
        sorted[sortedIndex: sortedIndex + mid - leftIndex + 1] = list[leftIndex:mid + 1]#왼쪽리스트에서 끝이 mid임
        #mid - leftIndex 왼쪽에 남은 인덱스크기임
    list[left:right + 1] = sorted[left:right + 1]#왼쪽 끝에서 오른쪽 끝까지 전부다 복사를 실시하는데 항상 인덱싱할 때는 끝에 1을 더해준다.


def mergeSort(list, left, right):
    if left < right:#왼쪽 값이 오른쪽 값보다 클때라는 거는 나누기해서 0이 나오기 전까지임
        mid = (left + right) // 2#중앙값을 구한다.
        mergeSort(list, left, mid)#왼쪽부분의 리스트에 대해서 재귀적으로 호출한다.
        mergeSort(list, mid + 1, right)#오른쪽에 대해서 재귀적으로 호출하기 위해서 사용
        merge(list, left, mid, right)#병합을 실시한다.


print("before sorting:", need_list)

mergeSort(need_list, 0, len(need_list) - 1)
print("after sorting:", need_list)
