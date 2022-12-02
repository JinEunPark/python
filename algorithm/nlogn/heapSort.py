def make_max_heap(list):
    length = len(list)
    for i in range(length//2,-1,-1):
        heapify(list,i)

    return list


def heapify(list, i):

    left = i*2 +1
    right = i*2 + 2
    index = i

    if left < len(list) and list[index] < list[left]:
        index = left
    if right < len(list) and list[index] < list[right]:
        index = right

    if index != i:#위의 조건문이 실행 되어서 index가 변경되었다면 재귀적으로 실행함
        list[i],list[index] = list[index], list[i]
        heapify(list,index)


arr = [14,235,2,3,2,34,1,5,1,6,23,1,6,34,5,23,4,32,41]
print(make_max_heap(arr))