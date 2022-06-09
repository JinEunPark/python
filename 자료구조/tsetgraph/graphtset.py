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
    visited = set([start])#시작점으로 주어진 정점을 방문한 리스트에 추가한다.
    que = [start]#너비 우선 탐색을 위해서 큐를 구현하는데 처음에 주어진 변수를 enqeue해서 초기화한다.
    while len(que) != 0:#큐의 길이가 0이 아닐때 까지
        vertex = que.pop(-1)#큐에 저장되어있던 정점을 뺀다.
        print(vertex, end=' ')#정점을 출력한다.
        neighborhood = graph[vertex] - visited#이미 방문한 정점을 제외하고 이웃 집합을 만든다.
        for v in neighborhood:#반복문을 통해서 이미 방문한 요소들을 추가한다.
            visited.add(v)#방문합 집합에 정점을 추가하는 동시에 큐에 정점들을 추가한다.
            que.append(v)


print()
BST('A', adjset)
