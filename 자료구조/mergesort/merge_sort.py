import random

sorted = [0]*10


def merge(list, left, mid, right):
    global sorted  # 글로벌로 선언된 정렬 리스트
    newIndex = left  # 병합해서 만들 새로운 리스트의
    Lindex = left
    Rindex = mid + 1
    while Lindex <= mid and Rindex <= right:
        if list[Lindex] < list[Rindex]:
            sorted[newIndex] = list[Lindex]
            newIndex += 1
            Lindex += 1
        else:
            sorted[newIndex] = list[Rindex]
            newIndex += 1
            Rindex += 1
    if Lindex > mid:  # 이 조건문을 만족하면 왼쪽은 새로운 리스트에 포함되었다는 거고 남은 오른쪽을 채워야한다.
        sorted[newIndex:newIndex + right - Rindex + 1] = list[Rindex:right + 1]
    else:  # 이 조건문을 만족하면 오른쪽은 새로운 리스트에 포함되었다는 거고 남은 왼쪽을 채워야한다.
        sorted[newIndex:newIndex + mid - Lindex + 1] = list[Lindex:mid + 1]

    list[left:right+1] = sorted[left:right+1]


def merge_sort(list, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(list, left, mid)  # 미드를 기준으로 다시 왼쪽 오른쪽으로 나눠서 호출
        merge_sort(list, mid + 1, right)  #
        merge(list, left, mid, right)  # 합병하면서 정렬이 진행된다.

list = [random.randrange(1,11)for i in range(10)]
print(list)
merge_sort(list, 0, 9)
print("after sort:", list)
