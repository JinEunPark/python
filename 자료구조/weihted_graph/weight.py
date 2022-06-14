# 인접행렬로 구현한 가중치 그래프
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weightlist = [[None, 29, None, None, None, 10, None],  # a
              [29, None, 16, None, None, None, 15],  # b
              [None, 16, None, 12, None, None, None],  # c
              [None, None, 12, None, 22, None, 18],  # d
              [None, None, None, 22, None, 27, 25],  # e
              [10, None, None, None, 27, None, None],  # f
              [None, 15, None, 18, 25, None, None]]


# 그래프내에 존재하는 모든 간선의 가중치의 합
def weight_sum(graph):
    sum = 0  #
    for i in range(len(graph)):
        for e in range(i + 1, len(graph)):  # 여기에서도 포문의 범위가 중요한데 i+1!! 기억할 것
            if graph[i][e] is not None:  # 간선이 존재한다면
                sum += graph[i][e]  # 합에 더함
    return sum


# 그래프 내의 모든 간선을 출력하는 함수
def printAlledges(vertex, graph):
    for i in range(len(vertex)):
        for e in range(i + 1, len(vertex)):  # 이 포문의 범위가 중요한데 그 이유는 첫번째 반복문의 i
            # 보다 하나 앞에서 시작해서 상부 삼각형이 출력됨 따라서 양방형 간선이 한번만 출력됨
            if graph[i][e] is not None:
                print("(%c, %c, %d)" % (vertex[i], vertex[e], graph[i][e]), end=" ")


print()
print("sum of the weight", weight_sum(weightlist))
printAlledges(vertex, weightlist)
print()

weightset = {'A': set([('B', 29), ('F', 10)]),
             'B': set([('A', 29), ('C', 16), ('G', 15)]),
             'C': set([('B', 16), ('D', 12)]),
             'D': set([('C', 12), ('E', 22), ('G', 18)]),
             'E': set([('D', 22), ('F', 27), ('G', 25)]),
             'F': set([('A', 10), ('E', 27)]),
             'G': set([('B', 15), ('D', 18), ('E', 25)])}


# 인접 리스트를 이용한 가중치 그래프의 가중치의 합

def weight_sum2(graph):
    sum = 0
    for i in graph:  # 집합의 요소에서 딕셔너리의 키값이 반복문으로 출력됨
        for e in graph[i]:  # 딕셔너리의 키값을 이용해서 정점의 인접 튜플을 하나씩 출력
            sum += e[1]  # 가중치는 튜플에서 두번째 요소임

    return sum // 2


def printAllweightedEdges(graph):
    for i in graph:
        for e in graph[i]:
            print("(%s, %s, %d)" % (i, e[0], e[1]), end=" ")


print("sum of weight", weight_sum2(weightset))
printAllweightedEdges(weightset)

parent = []
set_size = 0


def init_set(nSets):
    global parent, set_size  # 전역 변수를 사용하겠다고 선언
    set_size = nSets  # 파라민터로 전달된 집합의 사이즈를 저장
    for i in range(nSets):  # set의 사이즈 만큼 반복
        parent.append(-1)  # 부모를 나타내는 집합에 -1로 초기화


def find(id):  # 집합의 root노드의 id를 반환하는 함수
    while parent[id] >= 0:  # 노드의 자식이 -1이라면 자식이 위에 부모가 없는거고 그러면 정점 루트 노드임
        id = parent[id]  # 자식의 id를 부모의 id로 바꾼다.
    return id


def union(s1, s2):  # s1와 s2를 연결해 하나의 집합으로 만드는 함수인데 s2가 부모이다.
    global set_size
    parent[s1] = s2  # s1의 부모 id로 s2를 등록함
    set_size = set_size - 1  # 두개의 집합이 합쳐져서 집합의 총 갯수가 줄어듦


def MSTKruskal(vertex, adjlist):
    vertexSize = len(vertex)  # 정점의 갯수 저장
    init_set(vertexSize)  # 정점의 갯수만큼 부모 리스트 초기화
    eList = []  # 간선이 저장될 리스트

    for i in range(vertexSize - 1):  # 그냥 외워
        for j in range(i + 1, vertexSize):  # 상부 삼각행렬
            if adjlist[i][j] != None:  # 인접 행렬
                eList.append((i, j, adjlist[i][j]))  # 간선을 저장하는 리스트에 정점의 정보와 가중치를 튜플로 저장

    eList.sort(key=lambda e: e[2], reverse=True)  # 저장한 튜플의 마지막 요소인 가중치로 내림차순 정렬 갈수록 작아짐
    edgeAccepted = 0  # 간선의 수
    sum = 0
    while (edgeAccepted < vertexSize - 1):  # 신장트리는 간선의 갯수가 정점의 수 -1 개임
        e = eList.pop(-1)  # 가중치가 가장 작은 간선을 꺼냄
        uset = find(e[0])  # 간선을 연결하는 정점 1 집합의 대표 정점을 반환
        vset = find(e[1])  # 간선으로 연결된 정점 2 집합의 대표 정점을 반환

        if uset != vset:  # 두 정점이 속한 대표 정점이 다르다면 이는 다른 집합에 속한 정점이라는 것임
            sum += e[2]
            print("간선 추가 : (%s, %s, %d)" % (vertex[e[0]], vertex[e[1]], e[2]))
            # 두집합을 하나로 합침
            union(uset, vset)
            edgeAccepted += 1  # 간선이 하나 추가됨
    return sum


print()
min = MSTKruskal(vertex, weightlist)
print(min)

INF = 9999


def choose_vertex(dist, found):  # 최소 정점을 찾는 함수
    min = INF  # 최소값 맥스로 초기화
    minpos = -1
    for i in range(len(dist)):  # 정점의 갯수만큼
        if dist[i] < min and found[i] == False:  # 저장된 최단거리중 가장 작고 아직 방문하지 않은 정점 선택
            min = dist[i]
            minpos = i
    return minpos  # 가장 작은 정점의 인덱스 반환


def shortest_path_dijkstra(vertex, adjlist, start):
    vsize = len(vertex)
    dist = list(adjlist[start])
    path = [start] * vsize
    found = [False] * vsize
    dist[start] = 0

    for i in range(vsize):  # 정점의 갯수만큼 반복
        print("step%2d:" % (i + 1), dist)  # 각단계의 최단거리 출력
        u = choose_vertex(dist, found)  # 방문하지 않는 정점들 중 가장 최소 정점 선택
        found[u] = True  # 최소 정점을 방문한것으로 바꿈

        for w in range(vsize):  # 모든 정점에 대해서 반복
            if not found[w]:  # 방문하지 않은 노드에 있다면
                if dist[u] + adjlist[u][w] < dist[w]:  # 직접가는 경로보다 위에서 선택한 제일 작은 경로를 거쳐서 가는 것이 더 짧다면
                    dist[w] = dist[u] + adjlist[u][w]  # 갱신
                    path[w] = u  # 이전 노드를 저장
    return path


vertex2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

weight = [[0, 7, INF, INF, 3, 10, INF],
          [7, 0, 4, 10, 2, 6, INF],
          [INF, 4, 0, 2, INF, INF, INF],
          [INF, 10, 2, 0, 11, 9, 4],
          [3, 2, INF, 11, 0, 13, 5],
          [10, 6, INF, 9, 13, 0, INF],
          [INF, INF, INF, 4, 5, INF, 0]]
print("Shortest_path_dijkstra algorithm")
start = 0
path = shortest_path_dijkstra(vertex2, weight, start)

for end in range(len(vertex)):
    if end != start:
        print("[최단경로 %s -> %s] %s" % (vertex2[start], vertex2[end], vertex2[end]), end=" ")
        while (path[end] != start):
            print("<- %s" % (vertex[path[end]]), end='')
            end = path[end]
        print("<- %s" % (vertex[path[end]]))



def floyd(vertex,weight):
    vsize = len(vertex)
    copy = list(weight)
    for i in range(weight):
        copy[i] = list(weight[i])
    for k in range(vsize):
        for i in range(vsize):
            for  j in range(vsize):
                if(copy[i][k] + copy[k][j] < copy[i][j]):
                    copy[i][j] = copy[i][k] + copy[k][j]
        print(copy)


import pandas as pd










