def solution(name):
    if set(name) == {'A'}:
        return 0

    answer = float('inf')
    for i in range(len(name) // 2): # 반 이상 움직일 필요 없음
        left = name[-i:]+name[:-i]
        right = name[i:]+name[:i]

        for n in [left, right[0]+right[:0:-1]]:
            while n and n[-1] == 'A':
                n = n[:-1]
                print(n)

            row_move = i + len(n)-1
            col_move = 0
            for c in map(ord, n):
                col_move += min(c - 65, 91 - c)

            answer = min(answer, row_move + col_move)

    return answer

name ='RABAMATAWADLAFAVAAE'
answer = 61

print(solution(name))
# input:BMOABA / answer:30
# input:LAABAA / answer:15
# input:AAAAAAAAJAAAA / answer:14
# input:SAAAAAARRM / answer:41
# input:RABAMATAWADLAFAVAAE / answer:78