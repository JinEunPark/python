vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
INF = 9999
adjlist = [[0, 7, INF, INF, 3, 10, INF],
           [7, 0, 4, 10, 2, 6, INF],
           [INF, 4, 0, 2, INF, INF, INF],
           [INF, 10, 2, 0, 11, 9, 4],
           [3, 2, INF, 11, 0, INF, 5],
           [INF, INF, INF, 4, 5, 0, INF],
           [10, 6, INF, 9, INF, INF, 0]]
dist = []  # 시작 정점으로부터의 최단경로 거리를 저장
found = []  # 방문한 정점 표시를 위해 사용, 최초 모든항목이 False
path = []  # 바로이전 정점을 저장, 이전 정점을 따라 시작 정저 ㅁ까지 가는 경로가 최단 경로임.


def choose_vertex(dist, found):
    min = INF  # 초기에 최솟값을 INF로 설정한다. 인접하지 않은 노드를 INF로 설정함
    minpos = -1  # 가중치가 양수라는 가저아하에 가장 작은 가중치를 음수로 초기화

    for i in range(len(dist)):  # 전체 노드의 갯수만큼 반복
        if dist[i] < min and found[i] == False:  # start에서 인접한 노드 만을 방문하기위해서 초기에 INF보다 작고 min
            min = dist[i]
            minpos = i
    return minpos  # 인접하면서 cost가 가장 작은 node의 인덱스를 반환한다.


def shortest_path_dijkstra(vertex, adjlist, start):
    vsize = len(vertex)  # 정점의 갯수를 반환
    dist = list(adjlist[start])  # 시작 정점에서 다른 정점까지의 인접행렬의 행을 리스트로 반환해서 dist에 저장 결과적으로 최소 비용이 담기는 배열
    path = [start] * vsize  # 바로 이전 정점을 저장. 이전 정점을 따라 시작 정점까지 가는 경로가 최단경로임
    found = [False] * vsize  # 배열 생성및 초기화 방문한 노드는 다시 방문하지 않는다.
    dist[start] = 0  # 시작 정점의 거리 0
    found[start] = True  # 시작 정점 이미 찾아짐

    for i in range(vsize):
        print("step %2d:" % (i + 1), dist)  # 단계별로 dist[] 출력용
        u = choose_vertex(dist, found)  # 현재 방문한 노드들중에 최단거리에 있는 노드를 반환한다.
        found[u] = True  # 가장작은 인덱스를 이미 방문한것으로 처리

        for w in range(vsize):
            if not found[w]:  # 파이선 if None은 None는 거짓으로 취급된다. 아직 방문한 노드가 아니라면
                if dist[u] + adjlist[u][w] < dist[
                    w]:  # 위에서 찾은 최소 dist인 u에서 다른 노드로 가는 경로가 전체 노드를 도는데 방문한 인접 노드에서도 방문할 수 없는 노드이면 무한대 값이 반환되기 때문에 교환이 일어나지 않는다.
                    dist[w] = dist[u] + adjlist[u][w]  # 최단거리 갱신
                    path[w] = u  # 이전 노드를 path에 저장 만약에 w = 2 이고 u = 4인 경우에는 바로 전 정점이 B의 정점의 바로 전 정점이 E가 되는거임
                    # 그러니까 path[2] = 4가 되는거여

    return path


print("shortest path by dijkstar algorithm")
start = 0  # 초기에 시작하는 노드 설정
path = shortest_path_dijkstra(vertex, adjlist, start)  # A에서 모든 노드로 진행하는 최단거리를 가진 path 반환

for end in range(len(vertex)):
    if end != start:
        print("[shrotest path: %s -> %s] %s" % (vertex[start], vertex[end], vertex[end]), end='')

    while (path[end] != start):  # 전 노드가 시작 노드가 되기 전까지 이동
        print(" <- %s" % (vertex[path[end]]), end='')
        end = path[end]
    print("<- %s" % (vertex[path[end]]))

ver = ['S', 'A', 'B', 'C', 'D', 'E']
new = [[0, 14, 7, 9, INF, INF],
       [14, 0, INF, INF, INF, 9],
       [7, INF, 0, 10, 15, INF],
       [9, INF, 10, 0, 11, INF],
       [INF, INF, 15, 11, 0, 6],
       [INF, 9, INF, INF, 6, 0]]
print(shortest_path_dijkstra(ver,new,0))