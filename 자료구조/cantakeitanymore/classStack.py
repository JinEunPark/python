class stack:
    def __init__(self):
        self.top = []

    def isEmpty(self):
        return len(self.top) == 0

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if len(self.top) != 0:
            return self.top.pop(-1)  # -1 대신에 length of top 에 -1도 가능합니다.

    def peek(self):
        if len(self.top) != 0:
            return self.top[-1]

    def display(self):
        print(self.top)

    def __sizeof__(self):
        return len(self.top)

    def __str__(self):
        return str(self.top)
