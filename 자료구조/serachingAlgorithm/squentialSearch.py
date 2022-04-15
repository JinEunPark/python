list = [i for i in range(10)]

list2 = [1, 2, 3, 5, 3, 23, 5, 67, 8]


def squentialSearching(list, low, high, value):
    for i in range(low, high + 1):
        if value == list[i]:
            return i
    return None


def binarySearch(list, value):
    front = 0
    rear = len(list) - 1

    while front <= rear:
        mid = (front + rear) // 2
        if list[mid] == value:
            return mid
        if list[mid] > value:
            rear = mid - 1
        else:
            front = mid + 1


def interPolaration(list, value):
    high = len(list) - 1
    low = 0
    while high >= low:
        mid = int(low + (high - low) * ((value - list[low]) / (list[high] - list[low])))
        if list[mid] == value:
            return mid
        if list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return None


print(squentialSearching(list, 0, 8, 6))
print(binarySearch(list2, 67))
