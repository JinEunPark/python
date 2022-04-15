import random as random

list = [int(random.random() * 10) for i in range(11)]
list1 = [5, 6, 1, 2, 3, 4, 7, 8, 9, 0]  # 10 개의 랜덤한 정수를 만듦


def printinter(i, list):
    print("%d 번째 실행" % (i+1), list)


def selectionSorting(list):
    lenght = len(list)
    for i in range(lenght-1):
        least = i  # 겉 반복문을 이용해서 가장 작은 값의 인덱스를 표시하는 변수를 i로 초기화

        for e in range(i + 1, lenght):

            if list[least] > list[e]:
                least = e

        # list[least], list[i] = list[i], list[least]
        tmp = list[i]
        list[i] = list[least]
        list[least] = tmp
        printinter(i, list)
    return list


print(list1)
print(selectionSorting(list1))
