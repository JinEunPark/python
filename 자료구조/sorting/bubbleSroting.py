list = [3, 4, 1, 2, 6, 5, 7, 0, 8, 9]


# def bubbleSorting(list):
#     for i in range(len(list)-1):
#         left = i
#         right = i + 1
#         for e in range(0, len(list) - i -1):
#
#             if list[left] > list[right]:
#                 tmp = list[left]
#                 list[left] = list[right]
#                 list[right] = tmp
#                 left = right
#                 right = right + 1
#             else:
#                 left = right
#                 right = right + 1
#     return list

def bubbleSorting(list):
    for i in range(len(list) - 1, 0, -1):
        beChanged = False
        # 이중 반북문안에서 교환이 일어났는지 판단하기 위한 변수이다 첫번째 반복문을 실행할때 마다 거짓으로 초기화 켜서
        # 이중반복문안에서 교환이 일어나야지만 True로 바뀌게 만들어준다.

        for e in range(i):
            if list[e] > list[e + 1]:
                list[e], list[e + 1] = list[e + 1], list[e]
                # 두개를 비교해서 더 큰게 존재한다면 두 더 큰요소를 뒤로 땡긴다.
                beChanged = True
                # 교환이 일어난걸을 확인하기 위해서 교환이 일어나면 사실로 바꿔준다.

        if beChanged == False:
            return list
            # 교환이 일어날때 까지만 실행한다.


print(list)
print(bubbleSorting(list))
