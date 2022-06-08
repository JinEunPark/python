vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
INF = 9999
adjlist = [[0, 7, INF, INF, 3, 10, INF],
           [7, 0, 4, 10, 2, 6, INF],
           [INF, 4, 0, 2, INF, INF, INF],
           [INF, 10, 2, 0, 11, 9, 4],
           [3, 2, INF, 11, 0, 13, 5],
           [10, 6, INF, 9, 13, 0, INF],
           [INF, INF, INF, 4, 5, INF, 0]]

def printState(list):
    size = len(list)
    print("============================================================================================")
    for i in range(size):
        for e in range(size):
            if list[i][e] == INF:
                print("INF",end=' ')
            else:
                print(list[i][e], end = ' ')
        print()
def floydSearchShortest(vertex,adjlist):
    copylist = list(adjlist)
    for i in range(len(adjlist)):
        copylist[i] = list(adjlist[i])#배열을 생성하고 복사하는 과정
    for k in range(len(copylist)):
        for e in range(len(copylist)):
            for i in range(len(copylist)):
                if copylist[i][e] > copylist[i][k] + copylist[k][e]:
                    copylist[i][e] = copylist[i][k] + copylist[k][e]
        printState(copylist)

floydSearchShortest(vertex, adjlist)