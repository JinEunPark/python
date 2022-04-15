import random as random

list = [int(random.random() * 10) for i in range(11)]
print(list)


# 오름차순으로 정렬하는 방법
def findMin(list):
    for i in range(len(list) - 1):
        least = i
        for j in range(i + 1, len(list)):
            if list[least] > list[j]:
                tmp = list[i]
                list[least] = list[j]
                list[j] = tmp


findMin(list)
print(list)


def insertSorting(list):
    lenght = len(list)

    for i in range(lenght):
        key = list[i]
        j = i - 1
        while j > 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key


def binarySearch(list, key):
    high = len(list) - 1
    low = 0
    while True:
        middle = (high + low) // 2
        if list[middle] == key:
            return middle
        elif list[middle] < key:
            high = middle - 1
        elif list[middle] > key:
            low = middle + 1
