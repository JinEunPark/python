array = [1, 441, 63, 57, 45, 23, 54, 5645, 74, 8, 9, 8594, 67, 3, 9, 58, 2]


def insertionSorter(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while array[j] > key and j >= 0:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


insertionSorter(array)
print(array)


def mergeSort(alist, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(alist, p, q)
        mergeSort(alist, q + 1, r)
        merge(alist, p, q, r)


def merge(alist, p, q, r):
    left = q - p + 1
    right = r - q
    mid = q

    Llist = []
    Rlist = []

    for i in range(left):
        Llist.append(alist[p + i])
    for j in range(right):
        Rlist.append(alist[q + j + 1])
    print(Llist, Rlist)

    i = 0
    j = 0
    index = 0

    for k in range(p, r):

        if len(Llist) > i and len(Rlist) > j:
            if Llist[i] < Rlist[j]:
                alist[k] = Llist[i]
                i += 1
            else:
                alist[k] = Rlist[j]
                j += 1

        index = k
        break


    while i < len(Llist):
        alist[index+1] = Llist[i]
        index += 1
        i += 1

    while j < len(Rlist):
        alist[index+1] = Rlist[j]
        index += 1
        j += 1


mergeSort(array, 0, len(array) - 1)
print(array)
