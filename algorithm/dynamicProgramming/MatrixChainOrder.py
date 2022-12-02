import sys

cols = 6
rows = 6
p = [6, 5, 4, 10, 4, 5, 7]  # 메트릭스의 차원 배열 a[i] = 차원의 수를 가진다 길이가 행렬의 수보다 하나가 많음


def Matrix_Chain_Order(p):
    n = len(p) - 1  # 행렬의 수를 만듦

    matrix = [[0 for i in range(0, cols)] for e in range(0, rows)]  # m[i,j] table
    s = [[0 for i in range(0, cols)] for e in range(0, rows)]

    for i in range(0, n):
        matrix[i][i] = 0  # 대각 선상에 놓여있는 테이블에 대해서 0으로 초가화함.

    for i in range(0, n):  # 먼저 곱해지는 행렬의 갯수 이다 Ai...k의 길이가 l임

        for j in range(i + 1, n):  # Ak+1 ...n의 길이임.

            matrix[i][j] = sys.maxsize

            for k in range(i, j):

                result = matrix[i][k] + matrix[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if result < matrix[i][j]:
                    matrix[i][j] = result
                    s[i][j] = k

    return matrix, s


(m, s) = Matrix_Chain_Order(p)


def MatrixChainOrder(p):
    n = len(p)# 차수

    m = [[0 for x in range(n)] for x in range(n)]

    for L in range(2, n):

        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')#무한대 삽입

            for k in range(i, j):

                # q = cost/scalar multiplications
                q = m[i][k] + m[k + 1][j] + \
                	p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
    return m


new = MatrixChainOrder(p)


def printList(list):
    for i in range(len(list)):
        print(list[i])
        print()

print("my result------")
printList(m)

print("===================")
printList(new)
