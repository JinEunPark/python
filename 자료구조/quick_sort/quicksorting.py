def partition(list, left, right):
    low = left + 1
    high = right
    pivot = list[left]
    while (low <= high):
        while list[low] < pivot and low < right: low += 1  # 오른쪽 끝까지 이동가능하다
        while list[high] < pivot and high > left: high += 1  # 왼쩍 끝가지 이동이 가능하다.

        if low < high:
            list[high], list[low] = list[low], list[high]#선택된 위치의 값들의 자리를 변환한다.
    list[left], list[high] = list[high], list[left]# 마지막으로 pivot을 리스트의 제일 왼쪽에 있는 요소로 설정했으므로 이를 다시 교환하고
    return high# 위에서 high와 교환한 pivot의 값을 반환한다.


def quickSorting(list, left, right):
    if left < right:
        q = partition(list, left, right)
        quickSorting(list, left, q - 1)
        quickSorting(list, q + 1, right)
