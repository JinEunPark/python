class stack:
    def __init__(self):
        self.top = []

    def isEmpty(self):
        return len(self.top) == 0

    def push(self, item):
        self.top.append(item)

    def pop(self):
        return self.top.pop(-1)

    def peek(self):
        return self.top[-1]

    def size(self):
        return len(self.top)

    def clear(self):
        self.top = []

    def __str__(self):
        return str(self.top[::-1]) # [시작점 : 종료지점: 규칙] 이와 같이 설정하면 리스트를 반대로 만들어준다
