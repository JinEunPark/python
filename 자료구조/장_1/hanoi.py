def hanoi(n, frm, tmp, to):  # from에서 tmp를 이용해서 to로 이동하는 함수 이다. n 개의 원판을 옮기는 경우
    if n == 1:
        print("원판1: %s 에서 %s 로 이동하세요" % (frm, to))
    else:
        hanoi(n - 1, frm, to, tmp) # n 개의 원판을 옮기는 경우에는 frm에서 to를 이용해서 tmp로 n-1개의 원판을 옮겨야한다
        print("원판%d: %s에서 %s 로 이동하세요" % (n, frm, to))
        hanoi(n - 1, tmp, frm, to) # n-1개의 원판을 tmp 로 옮기고 나면 tmp에서 원판을 모두 다시 frm을 이용해서 to 로 옮겨야한다.


hanoi(3, 'A', 'B', 'C')
