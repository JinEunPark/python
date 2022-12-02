def quicksort(list, left, right):
    if left < right:
        p = partition(list, left, right)
        quicksort(list, left, p - 1)
        quicksort(list, p + 1, right)


def partition(list, left, right):
    pivot = list[right]
    r = right
    l = left
    for i in range(left, right):
        if list[i] <= pivot:
            l = + 1
            list[l], list[r] = list[r], list[l]
    list[l + 1], list[r] = list[r], list[l + 1]
    return l + 1
