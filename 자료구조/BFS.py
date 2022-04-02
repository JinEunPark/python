from circleQueue import circleQueue

map = [['1', '1', '1', '1', '1', '1'],
       ['0', '0', '1', '0', '0', '1'],
       ['1', '0', '0', '0', '1', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '0', '1', '0', '0', 'x'],
       ['1', '1', '1', '1', '1', '1'], ]
maplen = len(map)


class BFS(circleQueue):

    def __init__(self):
        super(BFS, self).__init__()  # circlequeue 를 생성
        self.que = circleQueue()

    def isVaildPos(self, x, y):
        if x < 0 or y < 0 or x > maplen - 1 or y > maplen - 1:
            return False
        elif map[x][y] == '1' or map[x][y] == 'x':
            return True

    def serachBFS(self):
        x = 0
        y = 0
        self.que.enqueue((1, 0))  # 시작 위치를 큐에 삽입

        while not self.que.isEmpty():
            here = self.que.dequeue()
            print(here, end="->")
            x, y = here
            if map[x][y] == 'x':
                return True
            else:
                map[x][y] = '.'
                if self.isVaildPos(x, y - 1): self.que.enqueue((x, y - 1))
                if self.isVaildPos(x, y + 1): self.que.enqueue((x, y + 1))
                if self.isVaildPos(x - 1, y): self.que.enqueue((x - 1, y))
                if self.isVaildPos(x + 1, y): self.que.enqueue((x + 1, y))
                print(self.que.list)

        return False


bfs = BFS()
result = bfs.serachBFS()
if result:
    print("---> 성공")
else:
    print("---> 실패")
