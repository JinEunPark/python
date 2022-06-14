# 인접향렬로 표현하 그래프이다.
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjlist = [[0, 1, 1, 0, 0, 0, 0, 0],
           [1, 0, 0, 1, 0, 0, 0, 0],
           [1, 0, 0, 1, 1, 0, 0, 0],
           [0, 1, 1, 0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 1, 1],
           [0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 1, 0],
           [0, 0, 0, 0, 1, 0, 1, 0],
           [0, 0, 0, 0, 0, 1, 1, 0]]
# 인점 집합으로 표현한 집합이다 집합내부의 요소들은 딕셔너리 형태로 표현되는데 내부의 요소들은 딕셔너리 형태이다.
adjset = {'A': set(['B', 'C']),
          'B': set(['A', 'D']),
          'C': set(['A', 'D', 'E']),
          'D': set(['B', 'C', 'F']),
          'E': set(['C', 'G', 'H']),
          'F': set(['D']),
          'G': set(['E', 'H']),
          'H': set(['E', 'G'])}


def DFS(graph, start, visited=set()):
    if start not in visited:  # start가 아직 방문한 집합에 포함도지 않는다면
        visited.add(start)  # 집합안에 start를 추가해서 이미 방문한것을 표시한다.
        print(start, end=" ")  # visited안에 넣고 이를 출력한다.
        neighborhood = graph[start] - visited  # 현재 정점의 이웃한 vertex들 중 이미 방문한 정점들을 제외하고 neighborhood를 만든다.
        for v in neighborhood:
            DFS(graph, v, visited)  # 순횐를 통해서 이웃주민들을 호출하는데 이때 각 이웃 주민의 첫번재 요소 부터 출력이 되니까 DFS가 된다.


DFS(adjset, 'A', set())


def BST(start, graph):
    visited = set([start])  # 시작점으로 주어진 정점을 방문한 리스트에 추가한다.
    que = [start]  # 너비 우선 탐색을 위해서 큐를 구현하는데 처음에 주어진 변수를 enqeue해서 초기화한다.
    while len(que) != 0:  # 큐의 길이가 0이 아닐때 까지
        vertex = que.pop(-1)  # 큐에 저장되어있던 정점을 뺀다.
        print(vertex, end=' ')  # 정점을 출력한다.
        neighborhood = graph[vertex] - visited  # 이미 방문한 정점을 제외하고 이웃 집합을 만든다.
        for v in neighborhood:  # 반복문을 통해서 이미 방문한 요소들을 추가한다.
            visited.add(v)  # 방문합 집합에 정점을 추가하는 동시에 큐에 정점들을 추가한다.
            que.append(v)


print()
BST('A', adjset)


# 신장 트리를 만드는 알고리즘인데 깊이 우선 탐색이나 너비 우선탐색을 할 때 과정을 그대로 출력하면 구현이 쌉 가능하다
def BstST(start, graph):
    visited = set([start])
    que = [start]
    while len(que) != 0:
        vertex = que.pop(0)
        neighborhood = graph[vertex] - visited
        for v in neighborhood:
            print("(", vertex, ",", v, ")", end=" ")  # 간선을 반복문을 통해서 출력한다.
            visited.add(v)
            que.append(v)


print()
BstST('A', adjset)


def dfs_cc(graph, vertex, color, visited):#열결성분검사에서 사용되는되는 것
    if vertex not in visited:#정점이 아직 방문되지 않았다면
        visited.add(vertex)#방문된 정점 추가
        color.append(vertex)#라벨리스트에 추가
        neighborhood = graph[vertex] - visited#이미 방문한 요소들 제거
        for v in neighborhood:
            dfs_cc(graph, v, color, visited)#순환호출로 스택 구현
    return color#마지막에 정점들이 저장된 리스트를 반환한다.


my = {'A':set({'B','C'}), 'B':set(['A']), 'C':set(['A']), 'D':set(['E']), 'E':set(['D'])}


def find_connected_component(graph):
    visited = set([])#비어 있는 방문 리스트 생성
    colorlist = []

    for vertex in graph:
        if vertex not in visited:
            colorlist.append(dfs_cc(graph, vertex, [], visited))#한번 호출된게 반환되면 이어진 요소들은 리스트에 담겨서 반환된다.
            #이미 방문된 정점들은 위의 조전문에서 걸려서 실행이 되지 않는다.
    print(len(colorlist))


find_connected_component(my)
