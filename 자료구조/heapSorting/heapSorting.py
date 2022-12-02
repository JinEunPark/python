from 자료구조.heapSorting.heap import MaxHeap
import random


def heapSorting(datalist):
    maxHeap = MaxHeap()
    for i in datalist:
        maxHeap.insert(i)
    for e in range(1, len(datalist) + 1):  # range의 범위가 최대 -1이고 그리고 -1인덱스로 부터 시작하기 때문에 반드시 len(datalist)+1까지
        datalist[-e] = maxHeap.delete()


# 힙정렬을 사용할때 이를 변경하기 위해서

def heapify(arr, arrlen, i):
    largest = i
    left = i * 2 + 1  # 원래 힙을 사용한것이 아니고 리스트를 사용했기 때문에 인덱스0번을 사용해서 왼쪽 자식이 i*2 +1이다
    right = i * 2 + 2  # 인덱스 0 번을 사용한 list에서의 오른쪽 자식의 인덱스

    if left < arrlen and arr[i] < arr[left]: largest = left  # 왼쪽 자식이 더 크다면
    if right < arrlen and arr[largest] < arr[right]: largest = right  # 오른쪽 자식이 더 크다면

    if largest != i:  # 위의 if 문장이 실행되었다면
        tmp = arr[i]  # 부모와 자식간의 위치를 바꾼다.
        arr[i] = arr[largest]
        arr[largest] = tmp

        heapify(arr, arrlen, largest)  # 더 밑의 트리에서도 조건에 부합해야 하기 때문에 더 밑에 순환호출을 이용해서
        # 자식을 최값으로 잡고 다시 호출한다.


def heapSort(list):

    length = len(list)
    print("i=", 0, list)

    for i in range(length // 2, -1, -1):  # 완전트리에서 마지막 leaf는 이미 단일 노드로
        # 이미 힙의 조건을 만족하기 때문에 제외하기 위해서 length//2
        heapify(list, length, i)
        print("i=", i, list)

    print()

    for i in range(length - 1, 0, -1):  # list의 길이의 가장 마지막 인덱스 부터 차례대로 내려오면서 인덱스를 반환한다.

        tmp = list[i]  # 마지막 요소와 첫번째 요소를 교환한다.
        list[i] = list[0]
        list[0] = tmp

        heapify(list, i, 0)  # 함수를 호출하는데 arraylength 자리에 들어갈 파라미터에 i를 전달하는 것을 볼 수 있는데 이는
        # 오름차순으로 정렬하기 위해서 아래의 뒤로 교환한 가장큰값을 정렬대상에서 제외하기 위해서다.
        print("i=", i, list)


randlist = [int(random.randrange(1, 10)) for i in range(10)]
randlist2 = [int(random.randrange(1, 10)) for i in range(10)]
testlist = [5, 3, 8, 4, 9, 1, 6, 2, 7]

print("before sorting(heapSorting):", randlist)
heapSorting(randlist)
print("after sorting(heapSorting):", randlist)
print("result of sorting before:", testlist)
heapSort(testlist)
print("result of after sorting:", testlist)


