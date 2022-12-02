list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def partition(list, left, right):

    high = right#오른쪽에서 부터 내려올 인덱스
    low = left + 1#왼쪽에서 부터 올라갈 인덱스 여기서 중요한건 첫번재 요소를 피벗이라서 +1을 한다
    pivot = list[left]#제일 왼쪽에 있는 요소를 피벗으로 만든다.

    while low <= high:#로우가 범위안에 있을 때 까지
        while low <= right and list[low] < pivot: low += 1
        #right보다 작고 pivot보다 작을 때까지 반복(큰값이면 멈춤)

        while high >= left and list[high] > pivot: high -= 1
        #left 보다 크고 그리고 피벗보다 큰값일때 까지 반복(작은 값을 찾으면 반복문을 벗어난다.)

        if low < high:#로우가 범위안에 존재한다면

            list[low], list[high] = list[high], list[low]
            #list를 교환한다.;…;;;;;

    list[left], list[high] = list[high], list[left]#마지막으로 high값고 피벗 값의 위치를 교환한다.
    return high#피벗의 위치를 반환한다.


def quickSorting(list, left, right):
    if left < right:#왼쪽이 범위안에 있을 때 까지
        p = partition(list, left, right)#피벗값을 반환하는 함수

        quickSorting(list, left, p-1)
        #피벗을 기준으로 왼쪽 요소를 실행 피벗을 제외하고 정렬을 해야하기 때문에 왼쪽이 p-1이다.
        quickSorting(list, p + 1, right)
        #피벗을 기준으로 오른쪽 요소를 실행하는 것이기 때문에 p+1으로 범위를 가지고 실행한다.


print("before sorting:", list)
quickSorting(list, 0, len(list) - 1)
print("after sorting:", list)
