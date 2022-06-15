list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def partition(list, left, right):
    high = right
    low = left + 1
    pivot = list[left]
    while low <= high:
        while low <= right and list[low] < pivot: low += 1
        while high >= left and list[high] > pivot: high -= 1

        if low < high:
            list[low], list[high] = list[high], list[low]
    list[left], list[high] = list[high], list[left]
    return high


def quickSorting(list, left, right):
    if left < right:
        p = partition(list, left, right)
        quickSorting(list, left, p)
        quickSorting(list, p + 1, right)


print("before sorting:", list)
quickSorting(list, 0, len(list) - 1)
print("after sorting:", list)
