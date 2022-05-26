import collections

# graph = {'A': {'B', 'C'}, 'B': {'A', 'D'}, 'C': {'A', 'D', 'E'}, 'D': {'B', 'C', 'F'}, 'E': {'C', 'G', 'H'}, 'F': {'D'},
#          'G': {'E', 'H'}, 'H': {'E', 'G'}}
vertex = ['a', 'b', 'c', 'd', 'e']
M = [[0, 1, 1, 0, 0],
     [1, 0, 0, 1, 1],
     [1, 0, 0, 1, 0],
     [0, 1, 1, 0, 1],
     [0, 1, 0, 1, 0]]
vertex2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjsust = [[1, 2],
           [0, 3],
           [0, 3],
           [1, 2, 4],
           [2, 6, 7],
           [4, 7],
           [4, 6]]

mygraph = {'S': {'A', 'C', 'B'}, 'A': {'S', 'D'}, 'B': {'S', 'D'}, 'D': {'B', 'C'}, 'C': {'S', 'D'}}

graph2 = {'A': {'B', 'C'}, 'B': {'A', 'D'}, 'C': {'A', 'D', 'E'}, 'D': {'B', 'C', 'F'}, 'F': {'D'},
          'E': {'C', 'G', 'H'},
          'G': {'E', 'H'},
          'H': {'E', 'G'}}


def dfs(graph, start, visited=set()):  # 파라미터로 딕셔너리로 구현한 인접 리스트, 탐색을 시작할 vertex, 방문을 표시할 visited  = set()을 전달한다.

    if start not in visited:  # start가 아직 방문하지 않은 노드일 경우에
        visited.add(start)  # 방문하지 않은 vertex일 경우에는 start를 방문을 나타내는 집합에 추가
        print(start, end=' ')  # 방문하면서 내부의 요소를 출력
        nbr = sorted(graph[start] - visited)  # start를 키값으로 저장하고 있는 셋에서 이미 방문한 쎗과 차집합 연산을 통해서 제거함
        for i in nbr:
            dfs(graph, i, visited)  # 인접한 노드를 이용해서 재귀적으로 다시 호출한다.
            # 이 반복문이 이게 dfs인 이유이다 끝까지 재귀저으로 이동하고 if문의 조건에 맞지 않으면 None를 반환하기 때문에
            # 깊이 우선연란이라고 할 수 있다.


class myqueue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.raer = 0
        self.max = 10

    def isFull(self):
        return (self.front + 1) % self.max == self.raer

    def isEmpty(self):
        return self.front == self.rear

    def enqueue(self, data):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.max
            self.queue[self.rear] = data

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.max
            return self.queue[self.front]


def bfs(graph, start):

    que = myqueue()
    que.enqueue(start)  # 제일 먼저 삽입
    visited = set(start)

    while not que.isEmpty():
        vertex = que.dequeue()
        print(vertex, end=" ")
        nbr = graph[vertex] - visited
        for n in nbr:
            visited.add(n)#visited 집합에 넣어버림과 동시에 큐에 삽입한다.
            que.enqueue(n)


def dfs_cc(graph, color, vertex, visited):#파이선에서도 배열은 레퍼런스가 전해지기 때문에 파라미터로 전달되어질 set의 원본의 값이 변한다.
    if vertex not in visited:
        visited.add(vertex)#재귀함수에서도 다른함수에서 호출되어서 추가된 값이 저장된다.
        color.append(vertex)# 재귀함수에서도 다른함수에서 호출되어서도 값의 변경된 값이 유지가된디.
        nbr = graph[vertex] - visited# 차집합을 이용해서 이미 방문한 값을 제외시킨다.
        for i in nbr:
            dfs_cc(graph, color, i, visited)
    return color

def find_conneccted_componet(graph):
    visited = set() #방문을 점검할 집합을 생성함
    colorlist = [] # 분리된 그래프를 저장할 배열을 생성함

    for vtx in graph: #graph에 들어있는 원소를 차례대로 방문함
        if vtx not in visited:# 만약 방문한 집합에 들어있지않는 요소가 있다면
            color = dfs_cc(graph, [], vtx, visited)
            colorlist.append(color)

    print("그래프 연결성분의 개수:",len(colorlist))
    print(colorlist)

find_conneccted_componet(graph2)


dfs(graph2, 'A')

