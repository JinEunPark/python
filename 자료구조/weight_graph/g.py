vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # 그래프의 저점들의 집합

weight = [[None, 29, None, None, None, 10, None],
          [29, None, 16, None, None, None, 15],
          [None, 16, None, 12, None, None, None],
          [None, None, 12, None, 22, None, 18],
          [None, None, None, 22, None, 27, 25],
          [10, None, None, None, 27, None, None],
          [None, 15, None, 22, 25, None, None]]
# 인접행렬로 나타낸 가중치 그래프 가중치를 가진 링크만이 값을 가지고 있고 나머지는 0이다.

graph = (vertex, weight)


def getweigt(vertex, weight):
    sum = 0
    for i in range(len(vertex)):
        for e in range(i + 1,
                       len(vertex)):  # 모든리스트의 중복을 허용하지 않게하기 위해서 상부 삼각행렬만 돈다, 그리고 i+1을 해도 상관없는 이유는 주대각선인 다 0이기 때문이다.
            if weight[i][e] is not None:
                sum += weight[i][e]
    return sum


print("sum of weight", getweigt(vertex, weight))


def printAllEdges(vertex, weight):
    for i in range(len(vertex)):
        for e in range(i + 1, len(vertex)):
            if weight[i][e] != None and weight[e][i] != None:
                print("(%c %s %d)" % (vertex[i], vertex[e], weight[i][e]))


printAllEdges(vertex, weight)

graph = {'A': set([('B', 29), ('F', 10)]),  # 인접리스트
         'B': set([('A', 29), ('C', 16), ('G', 15)]),
         'C': set([('B', 16), ('D', 12)]),
         'D': set([('C', 12), ('E', 22), ('G', 18)]),
         'E': set([('D', 22), ('F', 27), ('G', 25)]),
         'F': set([('A', 10), ('E', 27)]),
         'G': set([('B', 15), ('D', 18), ('E', 25)])}


def getweight2(graph):
    sum = 0
    for i in graph:  # 딕셔너리의 키값을 반환함
        for e in graph[i]:  # 딕셔너리의 키값으로 value에 접근해서 이에 속한 딕셔너리를 반환한다
            sum += e[1]  # 튜플에서 가중치를 저정한 두번째 값을 저장한다.
    return sum // 2


def printAlledges2(graph):
    for i in graph:
        for e in graph[i]:
            print("(%c %c %d)" % (i, e[0], e[1]), end=' ')  # 출발지 , 목적지, 가중치


print(getweight2(graph))
print(printAlledges2(graph))

parent = []
set_size = 0


def init_set(nSets):
    global set_size, parent
    set_size = nSets
    for i in range(nSets):
        parent.append(-1)#parent 의 크기의 부모 테이블을 초기하ㅗ 한다. 초기화 갑은 자기 자신으 부모로 가지도옥 설정한다.


def find(id):#해당 노드의 루트 노드를 반혼하는 함수이다.
    while (parent[id] >= 0):
        id = parent[id]
    return id


def union(s1, s2):#집합을 만드는 함수
    global set_size
    parent[s1] = s2#부모 배열의 값으로 s2를 s1의 value 로 사용함.
    set_size = set_size - 1#합집합이 생성되어서 집합이 크기를 하나 줄임.
