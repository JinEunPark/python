vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjMat = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 0, 0],
          [1, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 1],
          [0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 1],
          [0, 0, 0, 0, 1, 0, 1, 0]]


class queue:

    def __init__(self):
        self.front = 0
        self.rear = 0
        self.que = [None] * 10
        self.max = 10

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.max

    def enqueue(self, data):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.max
            self.que[self.rear] = data

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.max
            data = self.que[self.front]
            return data


def dfs(vertex, adjMat, index=0, visited=set()):
    visited.add(vertex[index])
    print(vertex[index], end=" ")

    for i in range(len(adjMat)):

        if adjMat[index][i] == 1:

            if vertex[i] not in visited:
                dfs(vertex, adjMat, i, visited)


def bfs(vertex, adjMat, visited=set(), index=0):
    que = queue()
    que.enqueue(index)
    visited.add(index)
    while not que.isEmpty():
        index = que.dequeue()
        print(vertex[index], end=" ")
        for i in range(len(vertex)):
            if adjMat[index][i] == 1 and vertex[i] not in visited:
                visited.add(vertex[i])
                que.enqueue(i)


dfs(vertex, adjMat)
print()
bfs(vertex, adjMat)


def filbo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return filbo(n - 1) + filbo(n - 2)


def getsum(n):
    if n == 0:
        return 0
    else:
        return n + getsum(n - 1)


def checkPalum(string, n):
    size = len(string)
    if size // 2 == n:
        return True
    elif string[size - n - 1] == string[n]:
        return checkPalum(string, n + 1)
    else:
        return False


string = "hello"
string2 = "asdfdsa"
print(getsum(10))
print(checkPalum(string, 0))
print(checkPalum(string2, 0))

import numpy as np
test_array = np.array([[1,2,3,4,],[1,2,5,8],[1,2,3,4]],float)
print(test_array)








x = np.array(range(8))
x = x.reshape(2,-1)
print(x)













