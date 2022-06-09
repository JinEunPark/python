def partitionDP(list, low, high):
    if list[low] > list[high]:
        list[low], list[high] = list[low], list[high]





def dq_quick_sort(list, low, high):
    if low > high:
        leftPartition, rightPartition = partitionDP(list, low, high)
        dq_quick_sort(list, low, leftPartition)
        dq_quick_sort(list, leftPartition, rightPartition)
        dq_quick_sort(list, rightPartition, high)
