n = 5
lost = [2, 4]
reserve = [1, 3, 5]


def solution(n, lost, reserve):

    MAX = 1000
    MIN = -1000
    add = 0
    new_lost = []
    lost.sort()
    reserve.sort()

    for i in lost:
        if i in reserve:
            reserve.remove(i)
        else:
            new_lost.append(i)

    for i in range(len(new_lost)):
        for e in range(len(reserve)):
            if reserve[e]+1 == new_lost[i] or reserve[e]-1 == new_lost[i]:
                add +=1
                new_lost[i] = MAX
                reserve[e] = MIN

    answer = n - len(new_lost)
    answer += add


    return answer


print(solution(n, lost, reserve))
